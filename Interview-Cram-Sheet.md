# 🧠 Interview Cram Sheet — AI Engineer

**The one file to reread the day before an interview.** Shortest, densest form of
everything on the 60-day curriculum + system design. Source of truth is this `.md`;
run `python scripts/build_cram_docx.py` to refresh **Interview-Cram-Sheet.docx**.

> How this fills up: every `/save-session` appends the 5–10 crispest lines from the
> day's topic here, under the right heading. Placeholders (`⏳ …`) mean "not studied yet".

---

## ⚡ 60-second orientation

- **Framework for ANY system design Q:** Requirements (functional + non-functional +
  scale numbers) → API sketch → data model → high-level diagram → deep-dive the 1–2
  hard parts → bottlenecks / failure / tradeoffs → wrap-up.
- **Framework for ANY ML design Q:** Business metric → ML framing → data & labels →
  features → model (baseline → better) → offline metrics → online metrics / A-B →
  serving (batch vs realtime) → monitoring & retraining → failure modes.
- **When stuck:** say the tradeoff out loud. Interviewers grade reasoning, not recall.
- **Numbers to know cold:** L1 cache ~1ns · RAM ~100ns · SSD ~100µs · network RT ~0.5ms
  (same DC) · disk seek ~10ms · 1 day ≈ 86,400s · "1M req/day" ≈ 12 req/s avg.

---

## 1 · Python + SQL

### Day 1 — Python fundamentals & data structures  *(template example — replace after studying)*
- `list` dynamic array O(1) amortized append, O(n) insert/search; `tuple` immutable;
  `set`/`dict` hash O(1) avg lookup; `dict` keeps insertion order (3.7+).
- Mutable default arg trap: `def f(x, acc=[])` — `acc` is shared across calls.
- `is` = identity, `==` = value. Small ints (−5..256) and interned strings are cached.
- Shallow vs deep copy: `copy.copy` vs `copy.deepcopy`; slicing copies one level.
- Comprehensions faster than manual loops; generator `()` for lazy / large data.
- **Common Q:** "list vs tuple vs set" · "how is dict implemented" · "reverse a string".

### Day 2 — Functions, `*args`/`**kwargs`, scope & closures
> ⏳ Fills in after you study this topic.

### Day 3 — OOP in Python
> ⏳ Fills in after you study this topic.

### Day 4 — Iterators, generators & decorators
> ⏳ Fills in after you study this topic.

### Day 5 — Exception handling & debugging
> ⏳ Fills in after you study this topic.

### Day 6 — Memory management & performance
> ⏳ Fills in after you study this topic.

### Day 7 — Multithreading, multiprocessing & async
> ⏳ Fills in after you study this topic.

### Day 8 — NumPy fundamentals
> ⏳ Fills in after you study this topic.

### Day 9 — Pandas & data manipulation
> ⏳ Fills in after you study this topic.

### Day 10 — SQL: joins, subqueries, CTEs, windows, optimization
> ⏳ Fills in after you study this topic.

---

## 2 · Machine Learning Fundamentals

### Day 11 — Supervised vs unsupervised
> ⏳ Fills in after you study this topic.

### Day 12 — Linear & logistic regression
> ⏳ Fills in after you study this topic.

### Day 13 — Trees, Random Forest & ensembles
> ⏳ Fills in after you study this topic.

### Day 14 — XGBoost / LightGBM / boosting
> ⏳ Fills in after you study this topic.

### Day 15 — KNN, Naive Bayes & SVM
> ⏳ Fills in after you study this topic.

### Day 16 — Feature engineering & selection
> ⏳ Fills in after you study this topic.

### Day 17 — Splits & cross-validation
> ⏳ Fills in after you study this topic.

### Day 18 — Bias–variance, overfitting, regularization
> ⏳ Fills in after you study this topic.

### Day 19 — Evaluation metrics
> ⏳ Fills in after you study this topic.

### Day 20 — ML pipelines & end-to-end
> ⏳ Fills in after you study this topic.

---

## 3 · Deep Learning

### Day 21 — Neural networks & perceptrons
> ⏳ Fills in after you study this topic.

### Day 22 — Forward & backpropagation
> ⏳ Fills in after you study this topic.

### Day 23 — Activations, losses, optimizers
> ⏳ Fills in after you study this topic.

### Day 24 — CNNs & computer vision
> ⏳ Fills in after you study this topic.

### Day 25 — RNNs, LSTMs, sequence modelling
> ⏳ Fills in after you study this topic.

### Day 26 — PyTorch fundamentals
> ⏳ Fills in after you study this topic.

---

## 4 · LLM Fundamentals

### Day 27 — NLP fundamentals & embeddings
> ⏳ Fills in after you study this topic.

### Day 28 — Attention mechanism
> ⏳ Fills in after you study this topic.

### Day 29 — Transformer architecture
> ⏳ Fills in after you study this topic.

### Day 30 — Encoder vs decoder vs encoder–decoder
> ⏳ Fills in after you study this topic.

### Day 31 — Tokenization & context windows
> ⏳ Fills in after you study this topic.

### Day 32 — Pretraining & next-token prediction
> ⏳ Fills in after you study this topic.

### Day 33 — Fine-tuning, instruction tuning, LoRA/PEFT
> ⏳ Fills in after you study this topic.

### Day 34 — Inference: temperature, sampling, decoding
> ⏳ Fills in after you study this topic.

---

## 5 · RAG

### Day 35 — What is RAG & why
> ⏳ Fills in after you study this topic.

### Day 36 — Document ingestion & preprocessing
> ⏳ Fills in after you study this topic.

### Day 37 — Chunking strategies
> ⏳ Fills in after you study this topic.

### Day 38 — Embeddings & embedding models
> ⏳ Fills in after you study this topic.

### Day 39 — Vector DBs & similarity search
> ⏳ Fills in after you study this topic.

### Day 40 — Retriever design & hybrid search
> ⏳ Fills in after you study this topic.

### Day 41 — Reranking, context compression, optimization
> ⏳ Fills in after you study this topic.

### Day 42 — Advanced RAG + evaluation
> ⏳ Fills in after you study this topic.

---

## 6 · Agents / Agentic AI

### Day 43 — What is an AI agent
> ⏳ Fills in after you study this topic.

### Day 44 — Agent architecture & reasoning loops
> ⏳ Fills in after you study this topic.

### Day 45 — Tool / function calling
> ⏳ Fills in after you study this topic.

### Day 46 — Planning, memory, state
> ⏳ Fills in after you study this topic.

### Day 47 — Multi-agent systems
> ⏳ Fills in after you study this topic.

### Day 48 — Agent eval, reliability, guardrails, failure
> ⏳ Fills in after you study this topic.

---

## 7 · Backend + Production AI

### Day 49 — FastAPI & building AI APIs
> ⏳ Fills in after you study this topic.

### Day 50 — REST, auth, async backend
> ⏳ Fills in after you study this topic.

### Day 51 — Redis, caching, queues, background jobs
> ⏳ Fills in after you study this topic.

### Day 52 — Docker & containerization
> ⏳ Fills in after you study this topic.

### Day 53 — Production AI architecture
> ⏳ Fills in after you study this topic.

---

## 8 · MLOps / Cloud / System Design

### Day 54 — ML lifecycle & MLOps
> ⏳ Fills in after you study this topic.

### Day 55 — Model/data/version mgmt & CI/CD
> ⏳ Fills in after you study this topic.

### Day 56 — Cloud deployment & GPU/inference architecture
> ⏳ Fills in after you study this topic.

### Day 57 — AI/ML system-design interviews
> ⏳ Fills in after you study this topic.

---

## 9 · My Projects

### 30-second pitch
> ⏳ Write after Day 58: what it does · who for · your role · stack · impact/metric.

### Architecture one-liner
> ⏳ Fills in after Day 59.

### Hard questions & my answers ("why did you build it this way?")
> ⏳ Fills in after Day 60.

---

## 🏗️ System Design — quick recall

### Reusable building blocks (learn once, reuse everywhere)
| Block | Used in | One-line |
|---|---|---|
| Consistent hashing | distributed cache, KV store | minimise key remap when nodes change |
| Fan-out on write vs read | news feed, notifications | precompute vs compute-on-read; hybrid for celebrities |
| Geospatial index (geohash / quadtree) | Uber, Yelp | turn 2-D proximity into prefix / range lookups |
| Idempotency key | payments, checkout | dedupe retried writes; store result keyed by request id |
| Saga / outbox | checkout, order | distributed txn via local txn + events + compensation |
| Distributed lock / optimistic concurrency | ticket booking | prevent double-sell of one seat |
| Token bucket / sliding window | rate limiter, API gateway | shared counter in Redis for multi-server limits |
| Trie + top-k cache | autocomplete | prefix tree, precompute popular completions |
| Snowflake ID | anything sharded | time + machine + seq → sortable unique id, no central DB |
| CDN + adaptive bitrate | video, static assets | edge caching + multiple encoded renditions |
| WebSocket + message queue | chat, live updates | persistent conn for push; queue for ordering/offline |
| CQRS / read replicas | read-heavy systems | split write model from denormalised read model |

### The 20 — one-line recall

Full solution + architecture diagram for each: [`system-design/`](system-design/README.md).

| # | Problem | Key design choice | Main bottleneck / trade-off |
|---|---|---|---|
| 1 | **URL Shortener** | Pre-generated key pool — write path never hits the DB for a code | Single-region redirect latency for global users → CDN |
| 2 | **Rate Limiter** | Externalised atomic counter in Redis (`INCR`), token bucket | Redis throughput → shard keys by client_id; fail open |
| 3 | **Chat App** | Persistent WebSockets + per-conversation seq numbers + shared broker to route across gateways | Stateful connection tables (deliberate exception) |
| 4 | **News Feed** | Hybrid: push for normal users, pull/merge-at-read for celebrities | Write storm (push) vs read-time compute (pull) |
| 5 | **Notification System** | Pub/sub fan-out; one worker pool per channel; DLQ + backoff | Slow provider blocking others; per-user spam → debounce |
| 6 | **Web Crawler** | Distributed URL frontier, per-domain rate-limited queues; Bloom filter dedup | Frontier throughput → shard by domain hash |
| 7 | **File Storage (Dropbox)** | Content-hashed chunking (dedup + delta sync) + metadata/blob split + version vectors | Metadata query load if mixed with blob bytes |
| 8 | **Ride-Sharing (Uber)** | Geohash/quadtree index in-memory (Redis geo); expanding-radius query; ETA-aware ranking | Location-ping write volume → shard geo index by region |
| 9 | **Proximity (Yelp)** | Geohash index + aggressive caching of popular cells; simple TTL invalidation | Read volume on hot areas; static data → cache-friendly |
| 10 | **Video Streaming** | Async transcoding pipeline + CDN edge delivery + segmented ABR | Encoding cost/time; # of bitrate tiers vs experience |
| 11 | **E-Commerce Checkout** | Saga: chained local transactions + events + compensating actions | Last-unit inventory contention → atomic conditional decrement |
| 12 | **Payment System** | Idempotency key → stored result; periodic ledger-vs-provider reconciliation | Ambiguous outcomes under network failure (at-least-once + idempotency, not exactly-once) |
| 13 | **Ticket Booking** | Per-seat Redis `SET NX EX` lock with TTL hold; finalize only on payment success | Lock granularity — coarser than per-seat kills throughput |
| 14 | **Autocomplete** | In-memory trie, precomputed top-k per node; hourly offline rebuild; hot-prefix cache | Freshness vs a read path that never touches a DB |
| 15 | **Distributed Cache** | Consistent hashing on a ring + virtual nodes + replicate to next 1–2 nodes | Rehash storm on node add/remove (the ring solves it) |
| 16 | **Key-Value Store (Dynamo)** | Consistent-hash partitioning + N replicas + quorum `W+R>N` + hinted handoff | Coordination cost of strong-consistency quorums; per-request consistency choice |
| 17 | **Log / Metrics Aggregation** | Sidecar → Kafka → stream processor → time-series DB; tiered downsampling by age | Write throughput → decouple ingest with a queue; retention vs cost |
| 18 | **Job Scheduler (cron at scale)** | Leader election (Raft/etcd) for dispatch + per-job `SET NX EX` lock as backstop | Brief dual-leader window in a partition → the lock is the real guarantee |
| 19 | **ID Generator (Snowflake)** | 64-bit: timestamp · pre-assigned machine_id · per-ms sequence — zero coordination | Clock skew / backward NTP jumps → pause generation |
| 20 | **Full Platform Capstone** | Event bus behind the Post service; every subsystem is an independent async consumer | Synchronous coupling (the bus avoids it); name it early |

### AI system-design variants
> ⏳ Drill with `/study SD-AI-1..4`. RAG Q&A · LLM serving (batching / GPU / queue) ·
> recommender (candidate-gen vs ranking, feature store) · agent orchestration
> (tool loop, state, mid-conversation failure).
