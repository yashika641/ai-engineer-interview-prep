# System Design — reference solutions

20 most-asked problems, each with an architecture diagram (Mermaid, renders on GitHub), the deep dive on its named focus areas, and a 30-second recall table.

Naming: `SD-NN_Name.md`. AI-specific variants (SD-AI-*) are drilled live via `/study` and saved here by `/save-session`.

| # | Problem | Focus |
|---|---|---|
| 1 | [URL Shortener](SD-01_URL-Shortener.md) | key generation strategies, read-heavy caching |
| 2 | [Rate Limiter](SD-02_Rate-Limiter.md) | token bucket vs sliding window, distributed rate limiting across servers |
| 3 | [Chat Application](SD-03_Chat-Application.md) | WebSockets, message ordering, delivery guarantees |
| 4 | [News Feed](SD-04_News-Feed.md) | fan-out-on-write vs fan-out-on-read |
| 5 | [Notification System](SD-05_Notification-System.md) | pub/sub fan-out, multi-channel delivery, retry / dead-letter handling |
| 6 | [Web Crawler](SD-06_Web-Crawler.md) | BFS traversal at scale, dedup, politeness / per-domain rate-limiting |
| 7 | [File Storage / Sharing Service](SD-07_File-Storage-Service.md) | chunking, sync conflict resolution, metadata vs blob split |
| 8 | [Ride-Sharing App](SD-08_Ride-Sharing-App.md) | geospatial indexing, real-time location updates, matching |
| 9 | [Proximity / Location-Based Service](SD-09_Proximity-Service.md) | geospatial queries at scale |
| 10 | [Live Video Streaming / Video Platform](SD-10_Live-Video-Streaming.md) | encoding pipeline, CDN distribution, adaptive bitrate |
| 11 | [E-Commerce Checkout / Order System](SD-11_Ecommerce-Checkout.md) | distributed transactions, inventory consistency, the Saga pattern |
| 12 | [Payment System](SD-12_Payment-System.md) | idempotency, the exactly-once illusion, reconciliation |
| 13 | [Ticket Booking System](SD-13_Ticket-Booking-System.md) | concurrent booking of the same seat, race conditions, distributed locks |
| 14 | [Search Autocomplete / Typeahead](SD-14_Search-Autocomplete.md) | trie data structures, ranking by popularity, caching hot prefixes |
| 15 | [Distributed Cache](SD-15_Distributed-Cache.md) | consistent hashing, eviction, replication |
| 16 | [Key-Value Store](SD-16_Key-Value-Store.md) | partitioning, replication, consistency model choice |
| 17 | [Log / Metrics Aggregation System](SD-17_Log-Metrics-Aggregation.md) | high write throughput, time-series data, downsampling old data |
| 18 | [Distributed Job Scheduler](SD-18_Distributed-Job-Scheduler.md) | leader election, avoiding duplicate job execution across nodes |
| 19 | [ID Generator (Twitter Snowflake)](SD-19_ID-Generator.md) | unique IDs across distributed systems without a central bottleneck |
| 20 | [Full Platform Capstone (Twitter/Reddit-style)](SD-20_Full-Platform-Capstone.md) | feed + search + notifications + rate limiting, combined into one system |

## AI-specific variants (drill with `/study`)
- **SD-AI-1** — RAG-based Q&A system
- **SD-AI-2** — LLM API serving (request batching, GPU utilisation, queueing)
- **SD-AI-3** — Recommendation system (feature store, candidate gen vs ranking, realtime vs batch)
- **SD-AI-4** — AI agent orchestration pipeline (multi-step tool calls, state, mid-conversation failure)

## Anchor problems (get genuinely fluent — the rest recombine these)
URL shortener (1) · Chat (3) · News feed (4) · Ticket booking (13) · RAG Q&A (SD-AI-1)
