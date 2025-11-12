# Hypothesis Testing Guide for Grimoire

A practical reference for using property-based testing with Hypothesis in your
LeetCode solutions.

## When to Use Hypothesis

### ✅ Great for:

- **Testing properties/invariants** (not exact outputs)
- **Discovering edge cases** you didn't think of
- **Input with clear constraints** (sorted, positive, bounded, etc.)
- **Verifying algorithms work generally** beyond LeetCode examples
- **Arrays, strings, numbers** with simple constraints

### ❌ Skip when:

- LeetCode examples already cover edge cases well
- Testing exact outputs (use dataclass tests instead)
- Input constraints are too complex to generate
- You're still learning the problem (add after you understand it)

### 🤝 Use both:

Dataclass tests for **explicit cases** (LeetCode examples)
Hypothesis tests for **properties and edge case discovery**

---

## Common Strategies by Data Structure

### Arrays & Lists

```python
from hypothesis import given
from hypothesis import strategies as st

# Basic list of integers
@given(st.lists(st.integers()))
def test_basic_list(arr):
    pass

# Constrained lists
@given(st.lists(st.integers(-1000, 1000), min_size=0, max_size=100))
def test_bounded_list(arr):
    pass

# Sorted/non-decreasing arrays
@given(st.lists(st.integers()).map(sorted))
def test_sorted_array(arr):
    pass

# Non-empty lists
@given(st.lists(st.integers(), min_size=1))
def test_non_empty(arr):
    pass

# Fixed length
@given(st.lists(st.integers(), min_size=5, max_size=5))
def test_fixed_length(arr):
    pass

# Positive integers only
@given(st.lists(st.integers(min_value=1)))
def test_positive_ints(arr):
    pass

# Lists with duplicates guaranteed (pigeonhole principle)
@given(st.lists(st.integers(0, 5), min_size=10))
def test_with_duplicates(arr):
    pass
```

### Strings

```python
# ASCII strings
@given(st.text(alphabet=st.characters(min_codepoint=32, max_codepoint=126)))
def test_ascii_string(s):
    pass

# Lowercase letters only
@given(st.text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=0, max_size=100))
def test_lowercase(s):
    pass

# Alphanumeric
@given(st.text(alphabet=st.characters(whitelist_categories=('Ll', 'Lu', 'Nd'))))
def test_alphanumeric(s):
    pass

# Fixed length strings
@given(st.text(min_size=10, max_size=10))
def test_fixed_length_string(s):
    pass
```

### Numbers

```python
# Integers in range
@given(st.integers(-1000, 1000))
def test_bounded_int(n):
    pass

# Floats
@given(st.floats(min_value=0.0, max_value=1.0, allow_nan=False))
def test_probability(p):
    pass

# Pairs of numbers (for ranges, etc.)
@given(st.integers(), st.integers())
def test_two_numbers(a, b):
    # Ensure ordering if needed
    if a > b:
        a, b = b, a
    pass
```

### Tuples and Pairs

```python
# Fixed-size tuples
@given(st.tuples(st.integers(), st.integers(), st.text()))
def test_three_tuple(triple):
    x, y, name = triple
    pass

# Lists of pairs
@given(st.lists(st.tuples(st.integers(), st.integers()), max_size=50))
def test_coordinate_list(points):
    pass
```

---

## Composite Strategies for Complex Data

Use `@st.composite` decorator to build custom data generators:

```python
from hypothesis import strategies as st

@st.composite
def sorted_pairs(draw):
    """Generate (start, end) where start <= end."""
    a = draw(st.integers(0, 100))
    b = draw(st.integers(a, 100))  # Ensure b >= a
    return (a, b)

@given(sorted_pairs())
def test_range_problem(interval):
    start, end = interval
    assert start <= end
    # Your test here
```

### Example: Linked list nodes

```python
@st.composite
def linked_lists(draw, max_length=20):
    """Generate linked list as list of values."""
    return draw(st.lists(st.integers(), max_size=max_length))

@given(linked_lists())
def test_reverse_linked_list(values):
    # Build linked list from values
    # Test your reversal
    pass
```

### Example: Binary trees

```python
@st.composite
def binary_trees(draw, max_depth=4):
    """Generate binary tree as nested tuples: (value, left, right)."""
    if max_depth == 0 or not draw(st.booleans()):
        return None

    value = draw(st.integers(-100, 100))
    left = draw(binary_trees(max_depth=max_depth-1))
    right = draw(binary_trees(max_depth=max_depth-1))
    return (value, left, right)

@given(binary_trees())
def test_tree_traversal(tree):
    if tree is None:
        return
    # Test your traversal logic
    pass
```

---

## Writing Good Properties

Properties are **invariants that always hold**, not specific outputs.

### Common property patterns:

#### 1. Output constraints
```python
@given(st.lists(st.integers()))
def test_output_never_negative(arr):
    result = find_max_sum(arr)
    assert result >= 0  # Max sum is never negative
```

#### 2. Size relationships
```python
@given(st.lists(st.integers()))
def test_output_size(arr):
    result = remove_duplicates(arr)
    assert len(result) <= len(arr)  # Can't add elements
```

#### 3. Reversibility
```python
@given(st.lists(st.integers()))
def test_reverse_twice_is_identity(arr):
    original = arr.copy()
    reverse(arr)
    reverse(arr)
    assert arr == original
```

#### 4. Idempotence (doing it twice = doing it once)
```python
@given(st.lists(st.integers()))
def test_sort_is_idempotent(arr):
    sorted_once = sorted(arr)
    sorted_twice = sorted(sorted_once)
    assert sorted_once == sorted_twice
```

#### 5. Relationship to reference implementation
```python
@given(st.lists(st.integers()))
def test_same_as_builtin(arr):
    my_result = my_sort(arr.copy())
    builtin_result = sorted(arr)
    assert my_result == builtin_result
```

#### 6. Data structure invariants
```python
@given(st.lists(st.integers()))
def test_bst_property(values):
    tree = build_bst(values)
    # Property: left < root < right at every node
    assert is_valid_bst(tree)
```

---

## Using `assume()` for Conditional Tests

Sometimes you need to filter inputs:

```python
from hypothesis import assume

@given(st.integers(), st.integers())
def test_division(a, b):
    assume(b != 0)  # Skip cases where b is zero
    result = a / b
    assert result * b == a  # Within floating point error
```

**Warning**: Overusing `assume()` can make tests slow. Prefer building the
constraint into the strategy when possible.

---

## Practical Examples for LeetCode Topics

### Two Pointers

```python
@given(st.lists(st.integers()).map(sorted))
def test_two_sum_sorted(arr):
    """Test two-sum on sorted array with two pointers."""
    if len(arr) < 2:
        return

    target = arr[0] + arr[-1]
    result = two_sum_sorted(arr, target)

    # Property: if solution exists, sum equals target
    if result:
        i, j = result
        assert arr[i] + arr[j] == target
```

### Sliding Window

```python
@given(st.lists(st.integers(0, 100), min_size=1), st.integers(1, 10))
def test_max_sum_subarray(arr, k):
    assume(k <= len(arr))

    result = max_sum_subarray_size_k(arr, k)

    # Property: result is at least as large as any single window we check
    for i in range(len(arr) - k + 1):
        window_sum = sum(arr[i:i+k])
        assert result >= window_sum
```

### Binary Search

```python
@given(st.lists(st.integers()).map(sorted), st.integers())
def test_binary_search(arr, target):
    result = binary_search(arr, target)

    if result >= 0:
        # If found, should be at returned index
        assert arr[result] == target
    else:
        # If not found, shouldn't be in array
        assert target not in arr
```

### Dynamic Programming (check invariants)

```python
@given(st.lists(st.integers(0, 100), min_size=1))
def test_max_subarray_sum(arr):
    result = max_subarray_kadane(arr)

    # Property: result is at least max(arr) (single element subarray)
    assert result >= max(arr)

    # Property: result is at most sum(arr) if all positive
    if all(x >= 0 for x in arr):
        assert result <= sum(arr)
```

---

## Debugging Tips

### 1. Hypothesis found a failing case - now what?

Hypothesis prints the minimal failing input:
```
Falsifying example: test_foo(arr=[0, 1, 2])
```

**Add it to your dataclass tests:**
```python
TEST_CASES = [
    TestCase(input=[0, 1, 2], expected=..., description="found by hypothesis"),
    # ... other cases
]
```

### 2. Tests are too slow

- Reduce `max_size`, `max_depth`, or range of values
- Avoid overusing `assume()` - build constraint into strategy instead
- Use `@given(...).example([1, 2, 3])` to add specific cases without generation

### 3. Want to see generated examples

```python
from hypothesis import given, settings, Phase

@given(st.lists(st.integers()))
@settings(verbosity=Verbosity.verbose)  # Print examples
def test_something(arr):
    pass
```

---

## Template Integration

The cantrip template includes a commented-out Hypothesis section:

```python
# Property-based tests (uncomment when useful for discovering edge cases)
# @given(st.lists(st.integers(-1000, 1000), min_size=0, max_size=100))
# def test_problem_name_properties(input_data):
#     """Test invariants that should always hold."""
#     result = problem_name(input_data)
#     # Add your property assertions here
#     pass
```

**To use:**
1. Uncomment the imports at top of file
2. Uncomment the test function
3. Adjust the strategy to match problem constraints
4. Write properties (not expected values!)

---

## Further Resources

- **Hypothesis docs**: https://hypothesis.readthedocs.io/
- **Strategy reference**: https://hypothesis.readthedocs.io/en/latest/data.html
- **Property-based testing intro**: https://increment.com/testing/in-praise-of-property-based-testing/

## Invoke the Testing Sage Agent

When you want help generating test cases or properties for a problem:

```
Invoke testing-sage for [problem name]
```

The agent will:
- Analyze your problem constraints
- Suggest appropriate Hypothesis strategies
- Recommend properties to test
- Help debug failing property tests
