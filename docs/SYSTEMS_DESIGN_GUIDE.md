

# Systems Design Interview Prep Guide

A structured approach to mastering systems design interviews using the **incantations** package in grimoire.

## Philosophy

Systems design interviews test:
- **Breadth**: Knowledge of distributed systems concepts
- **Depth**: Understanding trade-offs and implementation details
- **Communication**: Explaining complex systems clearly
- **Pragmatism**: Making real-world engineering decisions

You're not expected to design Google from scratch. You're expected to demonstrate systematic thinking and technical judgment.

---

## The Interview Process

### Typical 45-60 Minute Flow

1. **Requirements Gathering (5-10 min)**
   - Clarify functional requirements
   - Establish non-functional requirements (scale, availability, latency)
   - Agree on scope

2. **Back-of-Envelope Estimation (5 min)**
   - Calculate traffic (QPS)
   - Estimate storage needs
   - Determine bandwidth requirements

3. **High-Level Design (10-15 min)**
   - Draw component diagram
   - Explain data flow
   - Identify major components

4. **Deep Dive (15-20 min)**
   - Interviewer picks 1-2 areas to go deep
   - Discuss trade-offs
   - Show implementation knowledge

5. **Follow-ups (5-10 min)**
   - Bottlenecks and scaling
   - Failure scenarios
   - Monitoring and operations

---

## Essential Concepts (The Fundamentals)

Master these before practicing full designs:

### 1. Scaling Basics
- Vertical vs horizontal scaling
- Load balancing (algorithms, health checks)
- Stateless vs stateful services
- **Implement**: Simple load balancer round-robin

### 2. Caching
- Cache-aside, write-through, write-back
- Eviction policies (LRU, LFU, FIFO)
- Cache invalidation strategies
- **Implement**: LRU cache, consistent hashing

### 3. Database Design
- SQL vs NoSQL (when to use each)
- Indexing strategies
- Normalization vs denormalization
- **Implement**: Simple B-tree, hash index

### 4. Database Scaling
- Replication (master-slave, multi-master)
- Sharding (hash-based, range-based, geo)
- CAP theorem implications
- **Implement**: Consistent hashing for sharding

### 5. Asynchronous Processing
- Message queues (Kafka, RabbitMQ, SQS)
- Pub/sub patterns
- Event-driven architecture
- **Implement**: Simple message queue

### 6. Networking
- HTTP/HTTPS, REST, GraphQL
- WebSockets for real-time
- CDN for static content
- DNS and load balancing

### 7. Reliability
- Redundancy and replication
- Circuit breakers
- Rate limiting
- Retries and exponential backoff
- **Implement**: Token bucket rate limiter

### 8. Data Storage Patterns
- BLOB storage (S3, GCS)
- Time-series databases
- Search indices (Elasticsearch)
- Graph databases

### 9. Microservices Patterns
- API gateways
- Service discovery
- Inter-service communication (gRPC, REST)
- Distributed tracing

### 10. Security & Auth
- Authentication (OAuth, JWT)
- Authorization (RBAC, ABAC)
- Encryption (at rest, in transit)
- API security (rate limiting, keys)

---

## Design Pattern Checklist

Use this mental checklist for every design:

### Architecture Patterns
- [ ] **Load Balancing**: How to distribute traffic?
- [ ] **Caching**: What to cache? Where? TTL strategy?
- [ ] **Database**: SQL or NoSQL? Why?
- [ ] **Sharding**: Shard if scale > 1 machine can handle
- [ ] **Replication**: For availability and read scaling
- [ ] **CDN**: For static content delivery
- [ ] **Message Queue**: For async processing
- [ ] **Rate Limiting**: Prevent abuse

### Communication Patterns
- [ ] **Synchronous**: REST APIs for request/response
- [ ] **Asynchronous**: Message queues for long operations
- [ ] **Real-time**: WebSockets for live updates
- [ ] **Batch**: Scheduled jobs for analytics

### Data Patterns
- [ ] **Hot/Cold Storage**: Frequently vs rarely accessed
- [ ] **Aggregation**: Pre-compute expensive queries
- [ ] **Archival**: Old data to cheaper storage

---

## Interview Framework (RADIO)

Use this to structure your approach:

### **R**equirements
- Functional: What must it do?
- Non-functional: Scale, latency, availability
- Constraints: Budget, time, existing systems

### **A**rchitecture
- High-level components
- Data flow
- Technology choices

### **D**ata Model
- Database schema
- Relationships
- Access patterns

### **I**nterface
- API design
- Request/response formats
- Authentication

### **O**ptimization & Trade-offs
- Bottlenecks
- Scaling strategies
- Cost vs performance

---

## 15 Essential System Designs

Practice these in order (Easy → Medium → Hard):

### Easy (Foundational Patterns)
1. **URL Shortener** - Hashing, base62 encoding, caching
2. **Pastebin** - Similar to URL shortener + text storage
3. **Rate Limiter** - Token bucket, sliding window
4. **Key-Value Store** - Consistent hashing, replication

### Medium (Multiple Components)
5. **Twitter Feed** - Fanout, timelines, caching
6. **Instagram** - Image storage, feed generation, CDN
7. **Uber** - Geolocation, matching, real-time updates
8. **Web Crawler** - Distributed crawling, deduplication, politeness
9. **Chat System** - Real-time messaging, presence, history
10. **YouTube** - Video upload, transcoding, CDN, recommendations
11. **Notification System** - Multi-channel, batching, reliability
12. **Search Autocomplete** - Trie, caching, ranking

### Hard (Complex Trade-offs)
13. **Distributed Cache (Memcached)** - Sharding, replication, hot keys
14. **Ticketmaster** - High concurrency, inventory, consistency
15. **Google Drive** - File sync, conflict resolution, versioning

---

## Back-of-Envelope Estimation Cheat Sheet

### Traffic Estimation
```
DAU = Daily Active Users
Requests/day = DAU * actions_per_user
QPS (Queries Per Second) = Requests/day / 86400
Peak QPS = QPS * 2-3 (assume 2-3x average)
```

### Storage Estimation
```
Storage/entity = avg_size_in_bytes
Total storage = num_entities * storage_per_entity * retention_years
Growth = new_entities_per_day * storage_per_entity * 365
```

### Bandwidth Estimation
```
Incoming = QPS * avg_request_size
Outgoing = QPS * avg_response_size
```

### Memory Estimation (for caching)
```
Cache 20% of hot data = total_data * 0.2
```

### Quick Reference Numbers
```
1 million = 10^6 = 1M
1 billion = 10^9 = 1B
1 trillion = 10^12 = 1T

1 KB = 10^3 bytes = 1,000 bytes
1 MB = 10^6 bytes = 1,000,000 bytes
1 GB = 10^9 bytes = 1,000,000,000 bytes
1 TB = 10^12 bytes

Seconds per day = 86,400 ~= 100K
```

---

## Common Scalability Patterns

### Pattern: Read-Heavy System (95% reads, 5% writes)
**Examples**: Twitter feed, Instagram, news sites

**Architecture**:
- Master-slave DB replication (multiple read replicas)
- Aggressive caching (Redis/Memcached)
- CDN for static content
- Cache-aside pattern

### Pattern: Write-Heavy System (50% writes or more)
**Examples**: Analytics, logging, metrics

**Architecture**:
- Sharded write-optimized DB (Cassandra, DynamoDB)
- Asynchronous writes via message queue
- Batch processing
- Eventually consistent

### Pattern: Low-Latency Requirements (< 100ms)
**Examples**: Chat, gaming, trading

**Architecture**:
- In-memory caching (Redis)
- Geo-distributed servers
- WebSockets for real-time
- Edge computing / CDN

### Pattern: High-Consistency Requirements
**Examples**: Banking, inventory, ticketing

**Architecture**:
- ACID transactions (PostgreSQL)
- Pessimistic locking
- Synchronous replication
- Two-phase commit if distributed

### Pattern: Large File Storage
**Examples**: YouTube, Dropbox, Instagram

**Architecture**:
- Object storage (S3, GCS)
- CDN for delivery
- Separate metadata DB
- Async processing pipeline

---

## Technology Choices Quick Reference

### Databases

| Type | Use Case | Examples |
|------|----------|----------|
| **Relational (SQL)** | Structured data, ACID, relationships | PostgreSQL, MySQL |
| **Document** | Flexible schema, JSON documents | MongoDB, CouchDB |
| **Wide-Column** | Time-series, high write throughput | Cassandra, HBase |
| **Key-Value** | Simple lookups, caching | Redis, DynamoDB |
| **Graph** | Relationships, social networks | Neo4j, JanusGraph |
| **Search** | Full-text search, analytics | Elasticsearch, Solr |

### Caching

| Type | Use Case | Notes |
|------|----------|-------|
| **Redis** | General purpose, data structures | In-memory, persistence optional |
| **Memcached** | Simple key-value, distributed | In-memory only, no persistence |
| **CDN** | Static content, media | CloudFlare, Akamai, CloudFront |

### Message Queues

| Type | Use Case | Notes |
|------|----------|-------|
| **Kafka** | Event streaming, high throughput | Persistent, ordered, replay |
| **RabbitMQ** | Task queues, routing | Flexible routing, transient |
| **SQS** | Simple queuing, AWS | Managed service, at-least-once |

### Storage

| Type | Use Case | Notes |
|------|----------|-------|
| **S3 / GCS** | Object storage, large files | Scalable, durable, cheap |
| **EBS / PD** | Block storage for VMs | Low latency, persistent |
| **EFS / Filestore** | Shared file systems | NFS-compatible |

---

## Interview Tips & Common Mistakes

### Do's ✅
- **Ask clarifying questions** before jumping to solutions
- **Think out loud** - verbalize your thought process
- **Start simple** - then iterate and optimize
- **Draw diagrams** - visual communication is key
- **Discuss trade-offs** - show you understand choices aren't free
- **Know the numbers** - be comfortable with estimation
- **Admit unknowns** - "I'm not familiar with X, but I'd approach it like Y"

### Don'ts ❌
- **Don't assume requirements** - ask first
- **Don't over-engineer** - start with MVP, then scale
- **Don't skip estimation** - shows you understand scale
- **Don't use buzzwords** without understanding
- **Don't say "just use X"** - explain WHY use X
- **Don't ignore the interviewer** - it's a conversation
- **Don't forget operations** - monitoring, logging, debugging

### Red Flags to Avoid
- "We'll just use Kubernetes" (without explaining why)
- "NoSQL is faster" (not always true)
- "Microservices solve everything" (they add complexity)
- Ignoring CAP theorem implications
- Single point of failure in design
- No mention of monitoring or failure handling

---

## Study Schedule for Interview Prep

### Week 1-2: Fundamentals
- [ ] Scaling basics (vertical/horizontal, load balancing)
- [ ] Caching (strategies, eviction, LRU implementation)
- [ ] Databases (SQL vs NoSQL, indexing)
- [ ] Implement: LRU cache, load balancer, consistent hashing

### Week 3-4: First Designs (Easy)
- [ ] URL shortener
- [ ] Pastebin
- [ ] Rate limiter
- [ ] Key-value store
- Practice explaining out loud, drawing diagrams

### Week 5-6: Advanced Concepts + Medium Designs
- [ ] Database scaling (sharding, replication)
- [ ] Message queues and async processing
- [ ] Design: Twitter feed, Instagram, Uber
- Focus on trade-offs and deep dives

### Week 7-8: Complex Designs + Mock Interviews
- [ ] Design: YouTube, Chat system, Ticketmaster
- [ ] Practice full 45-min mock interviews
- [ ] Review weak areas
- [ ] Practice estimation and API design

### Daily Practice (1-2 hours)
1. Study 1 fundamental concept (30 min)
2. Implement key algorithm in Python (30 min)
3. Practice 1 design problem (30 min)
4. Review and document (30 min)

---

## Resources

### Books (Skim, don't read cover-to-cover)
- "System Design Interview" by Alex Xu (Vol 1 & 2)
- "Designing Data-Intensive Applications" by Martin Kleppmann (reference)

### Online Courses
- Educative: "Grokking the System Design Interview"
- ByteByteGo (Alex Xu's YouTube/newsletter)
- System Design Primer (GitHub)

### Practice Platforms
- Pramp (free mock interviews)
- Interviewing.io (paid, real interviews)
- LeetCode discuss (system design section)

### Company Engineering Blogs
- Netflix Tech Blog
- Uber Engineering
- Twitter Engineering
- Instagram Engineering
- Read how real systems are built!

---

## Tracking Progress

Use `incantations/README.md` to track:
- [ ] Fundamentals mastered (10 concepts)
- [ ] Easy designs completed (4 designs)
- [ ] Medium designs completed (8 designs)
- [ ] Hard designs completed (3 designs)
- [ ] Mock interviews practiced (5+ sessions)

---

## Remember

**Systems design is about trade-offs, not perfect solutions.**

Every choice has pros and cons. Your job is to:
1. Understand the requirements
2. Propose a reasonable solution
3. Explain the trade-offs
4. Iterate based on feedback
5. Show you can think at scale

You're demonstrating how you think, not reciting perfect answers. Good luck! 🔮
