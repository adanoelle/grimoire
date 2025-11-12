"""Design [System Name] - System Design Practice

Source: [LeetCode/Educative/YouTube/etc] | Difficulty: [Easy/Medium/Hard]

# Problem Statement

[Clear description of what you're designing. Include scale requirements.]

# Requirements

## Functional Requirements
1. [What the system must do]
2. [Feature 2]
3. [Feature 3]

## Non-Functional Requirements
1. [Availability/Latency/Consistency goals]
2. [Scale requirements]
3. [Other constraints]

# Back-of-Envelope Estimation

## Traffic
- [Requests per day/month]
- [Reads vs writes ratio]
- [Peak traffic considerations]

## Storage
- [Data size per entity]
- [Total entities]
- [Growth rate]
- [Retention period]
- **Total**: X TB for Y years

## Bandwidth
- [Request size]
- [Response size]
- [Total bandwidth]: X GB/sec

## Summary
- [QPS (queries per second)]
- [Storage]
- [Bandwidth]

# High-Level Design

## Components
1. **[Component 1]**: Purpose
2. **[Component 2]**: Purpose
3. **[Component 3]**: Purpose

## Data Flow
1. [Step 1 of user request]
2. [Step 2]
3. [Step 3]

## ASCII Diagram
```
[Draw simple component diagram showing:
 - Clients
 - Load balancer
 - Application servers
 - Databases
 - Caches
 - Message queues
 - External services
]
```

# API Design

## Endpoint 1
```
[HTTP METHOD] /api/v1/[resource]
Request: { ... }
Response: { ... }
```

## Endpoint 2
```
[HTTP METHOD] /api/v1/[resource]
Request: { ... }
Response: { ... }
```

# Database Design

## Schema

### Table 1
```sql
CREATE TABLE table_name (
    id BIGINT PRIMARY KEY,
    field1 VARCHAR(255),
    field2 TIMESTAMP,
    INDEX idx_field1 (field1)
);
```

### Table 2
```sql
-- ...
```

## Database Choice
- **Option 1 (SQL)**: Pros/Cons
- **Option 2 (NoSQL)**: Pros/Cons
- **Recommendation**: [Choice] because [reasons]

# Deep Dive: [Critical Component]

## Problem
[What specific challenge needs solving?]

## Approach 1: [Name]
- **How it works**: [Description]
- **Pros**: [Benefits]
- **Cons**: [Drawbacks]
- **Complexity**: Time/Space

## Approach 2: [Name]
- **How it works**: [Description]
- **Pros**: [Benefits]
- **Cons**: [Drawbacks]
- **Complexity**: Time/Space

## Chosen Approach: [Name]
[Why this is best for our requirements]

# Implementation (Core Algorithm)
"""

from typing import *
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Entity:
    """Main entity in the system."""
    id: str
    field1: str
    created_at: datetime


class SystemCore:
    """Core logic for [critical component].

    This demonstrates understanding of the key algorithm/data structure
    needed for this system design.
    """

    def __init__(self):
        self.data = {}

    def key_operation(self, param: str) -> Any:
        """Implement the most critical operation.

        Time: O(?)
        Space: O(?)
        """
        pass


"""
# Scaling Considerations

## Database Scaling
- **Partitioning**: [Strategy - hash/range/geo]
- **Replication**: [Master-slave/multi-master]
- **Sharding key**: [What to shard on and why]

## Caching Strategy
- **What to cache**: [Data types]
- **Cache policy**: [Write-through/aside/back]
- **TTL**: [Duration and reasoning]
- **Eviction**: [LRU/LFU]

## Load Balancing
- **Algorithm**: [Round-robin/least-connections/hash]
- **Geo-distribution**: [Multi-region strategy]
- **Health checks**: [How to detect failures]

## Asynchronous Processing
- **Message Queue**: [Kafka/RabbitMQ/SQS]
- **Use cases**: [What operations are async]
- **Ordering guarantees**: [If needed]

# Trade-offs & Design Decisions

## [Decision 1]
- **Options**: A vs B
- **Chosen**: [Choice]
- **Reasoning**: [Why]
- **Trade-off**: [What you gain vs lose]

## [Decision 2]
- **Options**: X vs Y
- **Chosen**: [Choice]
- **Reasoning**: [Why]
- **Trade-off**: [What you gain vs lose]

# Follow-up Questions & Answers

**Q: [Common follow-up question]?**
A: [Your answer with technical details]

**Q: [How to handle edge case]?**
A: [Your approach]

**Q: [How to monitor/debug this]?**
A: [Metrics, logging, tracing strategy]

**Q: [What if scale increases 10x]?**
A: [Bottlenecks and how to address them]

# Monitoring & Operations

## Key Metrics
- [Metric 1]: [Why important]
- [Metric 2]: [Threshold/alert]
- [Metric 3]: [Dashboard view]

## Failure Scenarios
- **[Failure 1]**: Impact and mitigation
- **[Failure 2]**: Impact and mitigation
- **[Failure 3]**: Impact and mitigation

# Lessons Learned

- [Key insight 1 from this design]
- [Pattern/technique that was crucial]
- [Mistake you initially made]
- [Interview tip specific to this problem]

# Related Designs

- [Similar system 1]: Key differences
- [Similar system 2]: Shared patterns
- [Problem that uses similar techniques]
"""
