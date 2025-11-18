# Algorithm Templates - Muscle Memory Reference

Commit these templates to memory. In interviews, recognize the pattern and code the template automatically.

---

## 1. Binary Search

### Classic Binary Search (Find Exact Value)
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Not found
```

### Binary Search - Left-Most (First Occurrence)
```python
def binary_search_left(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid  # Could be answer, keep searching left

    return left  # Returns insertion point if not found
```

### Binary Search - Right-Most (Last Occurrence)
```python
def binary_search_right(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] <= target:
            left = mid + 1  # Could be answer, keep searching right
        else:
            right = mid

    return left - 1  # Returns last occurrence, or -1 if not found
```

### Binary Search on Answer Space (Predicate-based)
```python
def binary_search_answer(min_val, max_val):
    """Find minimum value where condition becomes True"""
    left, right = min_val, max_val

    while left < right:
        mid = left + (right - left) // 2

        if is_valid(mid):  # Replace with your condition
            right = mid  # mid works, try smaller
        else:
            left = mid + 1  # mid doesn't work, need larger

    return left  # Minimum value where condition is True
```

---

## 2. Two Pointers

### Opposite Ends (Palindrome, Two Sum Sorted)
```python
def two_pointers_opposite(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        # Process arr[left] and arr[right]

        if condition_met():
            return result
        elif need_larger_value():
            left += 1
        else:
            right -= 1

    return default_result
```

### Same Direction (Fast/Slow - Remove Duplicates)
```python
def two_pointers_same_direction(arr):
    slow = 0

    for fast in range(len(arr)):
        if should_keep(arr[fast]):  # Your condition
            arr[slow] = arr[fast]
            slow += 1

    return slow  # New length / position
```

### Fast & Slow Pointers (Cycle Detection)
```python
def detect_cycle(head):
    slow = fast = head

    # Phase 1: Detect if cycle exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # Cycle detected
            break
    else:
        return None  # No cycle

    # Phase 2: Find cycle start (optional)
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # Cycle start node
```

---

## 3. Sliding Window

### Variable Size Window (Most Common)
```python
def sliding_window_variable(arr):
    left = 0
    window_state = {}  # Track window contents
    result = 0

    for right in range(len(arr)):
        # Expand window: add arr[right]
        window_state[arr[right]] = window_state.get(arr[right], 0) + 1

        # Shrink window while invalid
        while window_invalid(window_state):
            window_state[arr[left]] -= 1
            if window_state[arr[left]] == 0:
                del window_state[arr[left]]
            left += 1

        # Update result with current valid window
        result = max(result, right - left + 1)

    return result
```

### Fixed Size Window
```python
def sliding_window_fixed(arr, k):
    window_sum = sum(arr[:k])
    result = window_sum

    for right in range(k, len(arr)):
        # Slide window: add right, remove left
        window_sum += arr[right]
        window_sum -= arr[right - k]

        result = max(result, window_sum)

    return result
```

### Sliding Window with Counter (Substrings)
```python
from collections import Counter

def sliding_window_counter(s, t):
    """Template for 'find substring containing all chars of t'"""
    need = Counter(t)
    window = {}
    left = 0
    valid = 0  # How many chars in 'need' are satisfied

    for right in range(len(s)):
        # Add s[right] to window
        char = s[right]
        window[char] = window.get(char, 0) + 1

        if char in need and window[char] == need[char]:
            valid += 1

        # Shrink window when valid (all chars found)
        while valid == len(need):
            # Update result here

            # Remove s[left] from window
            char = s[left]
            if char in need and window[char] == need[char]:
                valid -= 1
            window[char] -= 1
            left += 1

    return result
```

---

## 4. DFS (Depth-First Search)

### DFS - Recursive (Tree)
```python
def dfs_recursive(root):
    if not root:
        return base_case_value

    # Preorder: process current node first
    result = process(root.val)

    # Recurse on children
    left_result = dfs_recursive(root.left)
    right_result = dfs_recursive(root.right)

    # Postorder: process after children
    return combine(result, left_result, right_result)
```

### DFS - Iterative (Tree)
```python
def dfs_iterative(root):
    if not root:
        return

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Add children (right first so left is processed first)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result
```

### DFS - Graph (with visited set)
```python
def dfs_graph(graph, start):
    visited = set()
    result = []

    def dfs(node):
        if node in visited:
            return

        visited.add(node)
        result.append(node)

        for neighbor in graph[node]:
            dfs(neighbor)

    dfs(start)
    return result
```

### DFS - Iterative (Graph)
```python
def dfs_graph_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

    return result
```

---

## 5. BFS (Breadth-First Search)

### BFS - Tree (Level Order)
```python
from collections import deque

def bfs_tree(root):
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result
```

### BFS - Level Order (with levels separated)
```python
def bfs_level_order(root):
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result
```

### BFS - Graph (Shortest Path)
```python
def bfs_graph(graph, start, target):
    queue = deque([(start, 0)])  # (node, distance)
    visited = {start}

    while queue:
        node, dist = queue.popleft()

        if node == target:
            return dist

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1  # Not found
```

---

## 6. Backtracking

### Backtracking - General Template
```python
def backtrack(nums):
    result = []

    def dfs(path, start):
        # Base case: valid solution found
        if is_valid_solution(path):
            result.append(path[:])  # Make a copy!
            return

        # Try all choices from current state
        for i in range(start, len(nums)):
            # Choose
            path.append(nums[i])

            # Explore
            dfs(path, i + 1)

            # Unchoose (backtrack)
            path.pop()

    dfs([], 0)
    return result
```

### Backtracking - Subsets
```python
def subsets(nums):
    result = []

    def dfs(start, path):
        result.append(path[:])  # Every path is a valid subset

        for i in range(start, len(nums)):
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()

    dfs(0, [])
    return result
```

### Backtracking - Permutations
```python
def permutations(nums):
    result = []

    def dfs(path, remaining):
        if not remaining:
            result.append(path[:])
            return

        for i in range(len(remaining)):
            dfs(path + [remaining[i]], remaining[:i] + remaining[i+1:])

    dfs([], nums)
    return result
```

### Backtracking - Combinations (with target sum)
```python
def combination_sum(candidates, target):
    result = []

    def dfs(start, path, current_sum):
        if current_sum == target:
            result.append(path[:])
            return
        if current_sum > target:
            return  # Prune

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            dfs(i, path, current_sum + candidates[i])  # i, not i+1 for reuse
            path.pop()

    dfs(0, [], 0)
    return result
```

### Backtracking - Avoid Duplicates
```python
def subsets_with_dup(nums):
    nums.sort()  # Must sort first!
    result = []

    def dfs(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):
            # Skip duplicates: if current same as previous AND we didn't use previous
            if i > start and nums[i] == nums[i-1]:
                continue

            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()

    dfs(0, [])
    return result
```

---

## 7. Linked List Patterns

### Reverse Linked List (Iterative)
```python
def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev  # New head
```

### Reverse Linked List (Recursive)
```python
def reverse_list_recursive(head):
    if not head or not head.next:
        return head

    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None

    return new_head
```

### Find Middle of Linked List
```python
def find_middle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow  # slow is at middle
```

### Merge Two Sorted Lists
```python
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 if l1 else l2
    return dummy.next
```

---

## 8. Tree Traversal Templates

### Preorder (Root → Left → Right)
```python
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)
```

### Inorder (Left → Root → Right)
```python
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```

### Postorder (Left → Right → Root)
```python
def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

---

## 9. Monotonic Stack

### Next Greater Element
```python
def next_greater_element(nums):
    result = [-1] * len(nums)
    stack = []  # Stores indices

    for i in range(len(nums)):
        # While current is greater than stack top
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]

        stack.append(i)

    return result
```

### Monotonic Increasing Stack Template
```python
def monotonic_increasing(nums):
    stack = []

    for num in nums:
        # Pop elements greater than current (maintain increasing)
        while stack and stack[-1] > num:
            stack.pop()

        stack.append(num)

    return stack
```

---

## 10. Prefix Sum

### Basic Prefix Sum
```python
def build_prefix_sum(nums):
    prefix = [0]

    for num in nums:
        prefix.append(prefix[-1] + num)

    return prefix  # prefix[i] = sum of nums[0:i]

# Range sum query: sum(nums[left:right+1])
def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]
```

---

## 11. Union Find (Disjoint Set)

### Union Find Template
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already connected

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True  # Successfully connected

    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

---

## How to Memorize

1. **Write each template 5 times by hand** without looking
2. **Solve 3-5 problems per template** to internalize when to use it
3. **Create flashcards**: Pattern on front, template on back
4. **Practice on whiteboard**: Code without IDE autocomplete
5. **Teach someone**: Explain each template to solidify understanding

## Pattern Recognition Cheat Sheet

| Problem Type | Algorithm |
|--------------|-----------|
| Sorted array → find target | Binary Search |
| Two elements sum to target (sorted) | Two Pointers (opposite) |
| Contiguous subarray with constraint | Sliding Window |
| All combinations/subsets | Backtracking |
| Shortest path in unweighted graph | BFS |
| Explore all paths in tree/graph | DFS |
| Linked list cycle | Fast & Slow Pointers |
| Next greater/smaller element | Monotonic Stack |
| Range sum queries | Prefix Sum |
| Connected components | Union Find or DFS/BFS |

---

**Pro tip**: When you sit down for an interview, mentally review these templates in 60 seconds. Then when you see the problem, you're just selecting and customizing the right template.
