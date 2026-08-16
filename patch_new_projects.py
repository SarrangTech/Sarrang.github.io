#!/usr/bin/env python3
"""
Patch script — adds 4 new projects to the portfolio:
  fraud-detection-feature-store, realtime-delivery-promise-engine,
  product-docs-agent-pipeline-aws, clinical-trial-supply-chain-anomaly-detection (placeholder)
Run: python3 patch_new_projects.py index.html > index_patched.html
Then diff/verify, then replace index.html.
"""
import sys

with open(sys.argv[1], encoding='utf-8') as f:
    html = f.read()

# ── PATCH 1: four cards appended to the ML PROJECTS grid, after the Databricks card ──
CARDS = """    <div class="pc cr" onclick="openOv('featurestore')">
      <div class="pt">Kafka · Databricks Feature Store · Redis · Real-Time Scoring</div>
      <div class="pn">Fraud Detection Feature Store</div>
      <div class="ph">2.7–16.4ms end-to-end scoring against a 100ms budget — 0.9728 ROC-AUC</div>
      <p class="pd">Kafka → Spark Structured Streaming → Delta bronze → dbt behavioral features (velocity, spend, volatility) → Databricks Feature Store → Redis. A scoring request never recomputes a feature — it looks one up.</p>
      <div class="pills"><span class="pill">Databricks Feature Store</span><span class="pill">Kafka</span><span class="pill">Redis</span></div>
      <div class="psig"><span class="sc hot">10-section deep-dive</span><span class="sc">GitHub</span><span class="sc">12 screenshots</span></div>
    </div>
    <div class="pc cb" onclick="openOv('deliveryengine')">
      <div class="pt">Kafka · Snowflake · dbt · FastAPI</div>
      <div class="pn">Real-Time Delivery Promise Engine</div>
      <div class="ph">219ms served promise (500ms budget) — 61 tests passing against live Snowflake</div>
      <p class="pd">Kafka → Spark Streaming → Delta bronze + Snowflake RAW → dbt staging/intermediate/gold → FastAPI. Recalculates delivery promises incrementally as carrier, inventory, and warehouse events arrive.</p>
      <div class="pills"><span class="pill">Kafka</span><span class="pill">Snowflake</span><span class="pill">dbt</span></div>
      <div class="psig"><span class="sc hot">10-section deep-dive</span><span class="sc">GitHub</span><span class="sc">10 screenshots</span></div>
    </div>
    <div class="pc cp" onclick="openOv('docsagent')">
      <div class="pt">Amazon Bedrock · RAG · Medallion · AWS Lambda</div>
      <div class="pn">Product Docs Agent Pipeline</div>
      <div class="ph">0.87 relevance on a zero-keyword-overlap query — 178ms, ~$0.01/month</div>
      <p class="pd">Ingests GitHub docs, refines through bronze/silver/gold, embeds via Amazon Bedrock Titan V2, and serves top-k semantic search through an AWS Lambda an AI agent calls directly.</p>
      <div class="pills"><span class="pill">Amazon Bedrock</span><span class="pill">AWS Lambda</span><span class="pill">RAG</span></div>
      <div class="psig"><span class="sc hot">9-section deep-dive</span><span class="sc">GitHub</span><span class="sc">Live demo</span></div>
    </div>
    <div class="pc co" onclick="openOv('clinicaltrial')">
      <div class="pt">Supply Chain · Anomaly Detection · In Progress</div>
      <div class="pn">Clinical Trial Supply Chain Anomaly Detection</div>
      <div class="ph">Coming soon — repo scaffolded, build in progress</div>
      <p class="pd">Anomaly detection for clinical trial investigational product distribution — temperature excursions, site-level stockout risk, chain-of-custody gaps. Early-stage; check back soon.</p>
      <div class="pills"><span class="pill">In Progress</span></div>
      <div class="psig"><span class="sc">Coming soon</span><span class="sc">GitHub</span></div>
    </div>"""

target = """    <div class="pc cgr" onclick="openOv('databricks')">
      <div class="pt">Databricks · Medallion Architecture · MLflow · Delta Lake · Unity Catalog</div>
      <div class="pn">Fraud Detection Pipeline</div>
      <div class="ph">0.9585 ROC-AUC — end-to-end Bronze → Silver → Gold → ML in 18 minutes</div>
      <p class="pd">Auto Loader ingestion → PySpark Medallion transforms → GradientBoosting with MLflow tracking → Unity Catalog model registry → batch scoring. 284,807 transactions, 0.17% fraud rate. All 4 tasks orchestrated as a single Databricks Job.</p>
      <div class="pills"><span class="pill">Databricks</span><span class="pill">Delta Lake</span><span class="pill">MLflow</span></div>
      <div class="psig"><span class="sc hot">10-section deep-dive</span><span class="sc">GitHub</span><span class="sc">4 screenshots</span><span class="sc">3 tables</span></div>
    </div>
  </div>
</section>"""

replacement = target.replace("  </div>\n</section>", "") + "\n" + CARDS + "\n  </div>\n</section>"

if target in html:
    html = html.replace(target, replacement, 1)
    print("CARD OK: 4 project cards added", file=sys.stderr)
else:
    print("CARD FAIL: insertion point not found", file=sys.stderr)

# ── PATCH 2: routeMap entries ──
old_route = "  'databricks': 'databricks'\n};"
new_route = ("  'databricks': 'databricks',\n"
             "  'featurestore': 'featurestore',\n"
             "  'deliveryengine': 'deliveryengine',\n"
             "  'docsagent': 'docsagent',\n"
             "  'clinicaltrial': 'clinicaltrial'\n};")
if old_route in html:
    html = html.replace(old_route, new_route, 1)
    print("ROUTE OK: routeMap entries added", file=sys.stderr)
else:
    print("ROUTE FAIL: routeMap insertion point not found", file=sys.stderr)

# ── PATCH 3: overlays before </body> ──
OVERLAYS = r"""
<!-- ============ FRAUD DETECTION FEATURE STORE ============ -->
<div id="ov-featurestore" class="ov">
<button class="cbtn" onclick="closeOv()">← Back</button>
<div class="oh" style="background:linear-gradient(155deg,#1a0805 0%,#080808 60%)">
  <div class="otag" style="color:var(--r)">Kafka · Databricks Feature Store · Redis · Real-Time Scoring</div>
  <div class="oname">Fraud Detection Feature Store</div>
  <div class="ohead">Real-time transaction risk scoring backed by a Databricks-native feature store, with sub-100ms online decisioning served from Redis. A scoring request never recomputes a feature — it looks one up.</div>
  <div class="omets">
    <div class="omet"><div class="omn" style="color:var(--r)">0.9728</div><div class="oml">ROC-AUC</div></div>
    <div class="omet"><div class="omn" style="color:var(--g)">77.55%</div><div class="oml">Recall</div></div>
    <div class="omet"><div class="omn" style="color:var(--gr)">2.7–16.4ms</div><div class="oml">End-to-End Latency (100ms budget)</div></div>
    <div class="omet"><div class="omn" style="color:var(--b)">&lt;10ms</div><div class="oml">Redis Feature Lookup</div></div>
    <div class="omet"><div class="omn" style="color:var(--o)">15 min</div><div class="oml">Feature Freshness SLA</div></div>
  </div>
</div>
<div class="obody">
  <div class="osec">
    <div class="ostag">The Problem</div>
    <div class="ostit">Behavioral Features Do Not Fit a 100ms Scoring Budget</div>
    <div class="otxt">
      <p>Fraud decisions have to be made inline with the authorization request — typically inside a 100ms latency budget — but the signals that are most predictive of fraud are behavioral: how an account typically transacts, and how the current transaction deviates from that baseline. Computing that on demand means aggregating a user's transaction history over trailing 1h/24h/7d windows against a table of hundreds of thousands to billions of rows — hundreds of milliseconds to seconds, not the low single-digit milliseconds a scoring request can spend on a feature lookup.</p>
      <p>A feature store separates the two halves of the problem. Feature computation happens offline, on a schedule, using Spark/dbt/SQL. The output — one row per account, keyed for O(1) lookup — is materialized into Redis. This trades feature <strong>exactness</strong> for feature <strong>freshness</strong>, a tradeoff documented explicitly rather than left implicit.</p>
    </div>
  </div>
  <div class="osec">
    <div class="ostag">Architecture</div>
    <div class="ostit">Offline Compute, Online Lookup — Never the Reverse</div>
    <div class="flow">
      <div class="fstep"><div class="fsn">Ingest</div><div class="fsname">Kafka → Spark Streaming → Delta bronze</div></div>
      <div class="farr">→</div>
      <div class="fstep"><div class="fsn">Silver</div><div class="fsname">dbt: velocity, spend, volatility</div></div>
      <div class="farr">→</div>
      <div class="fstep"><div class="fsn">Feature Store</div><div class="fsname">Databricks FS (PK: user_id) → Redis</div></div>
      <div class="farr">→</div>
      <div class="fstep"><div class="fsn">Serve</div><div class="fsname">FastAPI: lookup → score → APPROVE/DECLINE</div></div>
    </div>
    <table class="ctbl">
      <thead><tr><th>Component</th><th>Path</th><th>Responsibility</th></tr></thead>
      <tbody>
        <tr><td>Ingestion</td><td>streaming/producer.py</td><td>Replays transactions onto Kafka, keyed by account for per-account ordering</td></tr>
        <tr class="hlrow"><td>Feature engineering</td><td>dbt/models/*</td><td>Leakage-safe window functions (RANGE BETWEEN … PRECEDING) — training input</td></tr>
        <tr><td>Feature Store</td><td>01_feature_store_registration.py</td><td>Registers account-level aggregate, versioned + lineage-tracked</td></tr>
        <tr class="hlrow"><td>Online sync</td><td>03_redis_feature_sync.py</td><td>Pushes Feature Store table into Redis, one hash per account</td></tr>
        <tr><td>Real-time scoring</td><td>serving/scoring_api.py</td><td>Only component in the live request path — everything else runs async</td></tr>
      </tbody>
    </table>
  </div>
  <div class="osec">
    <div class="ostag">Feature Definitions</div>
    <div class="ostit">Velocity, Spend Pattern, and Volatility — Not Raw Transaction Attributes</div>
    <div class="rgrid">
      <div class="rcard"><div class="rn" style="color:var(--r)">Velocity</div><div class="rl">Txn count in trailing 1h/24h/7d. Card testing and account takeover both manifest as a velocity deviation before amounts look unusual.</div></div>
      <div class="rcard"><div class="rn" style="color:var(--g)">Spend Patterns</div><div class="rl">Current amount vs. account's recent average/max. An order-of-magnitude jump against a low prior maximum is a standard fraud indicator.</div></div>
      <div class="rcard"><div class="rn" style="color:var(--gr)">Volatility</div><div class="rl">Trailing stddev + z-score of amount. A sudden variance spike is characteristic of an account being tested or drained.</div></div>
    </div>
  </div>
  <div class="osec">
    <div class="ostag">Model &amp; Latency Budget</div>
    <div class="ostit">GradientBoostingClassifier, Time-Split Evaluation, Recall-Tuned Threshold</div>
    <table class="ctbl">
      <thead><tr><th>Metric</th><th>Value</th></tr></thead>
      <tbody>
        <tr><td>ROC-AUC</td><td>0.9728</td></tr>
        <tr class="hlrow"><td>Recall</td><td>0.7755</td></tr>
        <tr><td>Precision</td><td>0.5846</td></tr>
        <tr class="hlrow"><td>F1</td><td>0.6667</td></tr>
        <tr><td>Average Precision</td><td>0.7561</td></tr>
      </tbody>
    </table>
    <table class="ctbl">
      <thead><tr><th>Stage</th><th>Budget</th><th>Observed</th></tr></thead>
      <tbody>
        <tr><td>Redis feature lookup</td><td>&lt;10ms</td><td>1.4–5.1ms</td></tr>
        <tr class="hlrow"><td>Feature vector assembly</td><td>&lt;1ms</td><td>&lt;1ms</td></tr>
        <tr><td>Model inference (~30 features)</td><td>&lt;15ms</td><td>1.1–13.7ms</td></tr>
        <tr class="hlrow"><td><strong>Total end-to-end</strong></td><td><strong>&lt;100ms</strong></td><td><strong>2.7–16.4ms</strong></td></tr>
      </tbody>
    </table>
    <div class="insight">Decision threshold is 0.30, not 0.50 — tuned toward recall, since a missed fraud case is materially costlier than an unnecessary decline in this domain. Every /score response logs actual feature_lookup_ms, scoring_ms, and total_ms.</div>
  </div>
  <div class="osec">
    <div class="ostag">Known Limitations</div>
    <div class="ostit">Documented By Design, Not Discovered By Accident</div>
    <div class="otxt"><p>Training deliberately never joins the online Feature Store table — it reads a point-in-time-safe silver table instead, because joining an all-time aggregate by account ID would leak future behavior into past transactions. Online serving trades exactness for freshness: it uses an all-time behavioral aggregate refreshed every 15 minutes, not a per-request recomputation, and the mapping between the two is centralized and explicit rather than implicit.</p></div>
    <div class="insight">Redis TTL cold-start failure mode: a flat 24-hour TTL means accounts that transact less than once a day get a zeroed-history feature vector on their next transaction — an artificially low fraud probability for infrequent-but-legitimate spenders. Documented as a known tradeoff, with a stated mitigation (activity-based TTL or population-level fallback).</div>
  </div>
  <div class="osec">
    <div class="ostag">Screenshots</div>
    <div class="ostit">Test Suite · Kafka · Feature Store · MLflow</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:2px;margin:20px 0">
      <div style="background:var(--m);border:1px solid var(--bd);overflow:hidden">
        <img src="https://raw.githubusercontent.com/SarrangTech/fraud-detection-feature-store/main/docs/screenshots/01_pytest_suite.png" alt="Test suite — 15 unit tests" style="width:100%;display:block;filter:brightness(0.92)" onerror="this.parentElement.innerHTML='<div style=&quot;padding:32px;font-family:DM Mono,monospace;font-size:10px;color:var(--mu);letter-spacing:.1em;text-transform:uppercase&quot;>Test suite screenshot — github.com/SarrangTech/fraud-detection-feature-store</div>'">
        <div style="padding:10px 14px;font-family:'DM Mono',monospace;font-size:9px;letter-spacing:.12em;text-transform:uppercase;color:var(--mu)">15 unit tests — producer, feature mapping, Redis client, scoring API</div>
      </div>
      <div style="background:var(--m);border:1px solid var(--bd);overflow:hidden">
        <img src="https://raw.githubusercontent.com/SarrangTech/fraud-detection-feature-store/main/docs/screenshots/03b_kafka_producer.png" alt="Kafka producer throughput" style="width:100%;display:block;filter:brightness(0.92)" onerror="this.parentElement.innerHTML='<div style=&quot;padding:32px;font-family:DM Mono,monospace;font-size:10px;color:var(--mu);letter-spacing:.1em;text-transform:uppercase&quot;>Kafka producer screenshot</div>'">
        <div style="padding:10px 14px;font-family:'DM Mono',monospace;font-size:9px;letter-spacing:.12em;text-transform:uppercase;color:var(--mu)">500 transactions streamed at 45.7 events/sec, 2% fraud</div>
      </div>
      <div style="background:var(--m);border:1px solid var(--bd);overflow:hidden">
        <img src="https://raw.githubusercontent.com/SarrangTech/fraud-detection-feature-store/main/docs/screenshots/06a_feature_store_overview.png" alt="Databricks Feature Store overview" style="width:100%;display:block;filter:brightness(0.92)" onerror="this.parentElement.innerHTML='<div style=&quot;padding:32px;font-family:DM Mono,monospace;font-size:10px;color:var(--mu);letter-spacing:.1em;text-transform:uppercase&quot;>Feature Store screenshot</div>'">
        <div style="padding:10px 14px;font-family:'DM Mono',monospace;font-size:9px;letter-spacing:.12em;text-transform:uppercase;color:var(--mu)">user_fraud_features registered — user_id primary key</div>
      </div>
      <div style="background:var(--m);border:1px solid var(--bd);overflow:hidden">
        <img src="https://raw.githubusercontent.com/SarrangTech/fraud-detection-feature-store/main/docs/screenshots/07_mlflow_experiment.png" alt="MLflow experiment run" style="width:100%;display:block;filter:brightness(0.92)" onerror="this.parentElement.innerHTML='<div style=&quot;padding:32px;font-family:DM Mono,monospace;font-size:10px;color:var(--mu);letter-spacing:.1em;text-transform:uppercase&quot;>MLflow screenshot</div>'">
        <div style="padding:10px 14px;font-family:'DM Mono',monospace;font-size:9px;letter-spacing:.12em;text-transform:uppercase;color:var(--mu)">GBM run — ROC-AUC 0.9728, recall 0.7755 @ threshold 0.30</div>
      </div>
    </div>
  </div>
  <div class="osec">
    <div class="ostag">Stack</div><div class="ostit">Built With</div>
    <div class="tools">
      <span class="ttag">Kafka</span>
      <span class="ttag">Spark Structured Streaming</span>
      <span class="ttag">Delta Lake</span>
      <span class="ttag">dbt</span>
      <span class="ttag">Databricks Feature Store</span>
      <span class="ttag">Redis</span>
      <span class="ttag">MLflow</span>
      <span class="ttag">Unity Catalog</span>
      <span class="ttag">FastAPI</span>
      <span class="ttag">scikit-learn</span>
      <span class="ttag">Docker</span>
    </div>
    <div class="olinks">
      <a href="https://github.com/SarrangTech/fraud-detection-feature-store" class="olink pri" target="_blank">GitHub →</a>
    </div>
  </div>
</div>
</div>

<!-- ============ REAL-TIME DELIVERY PROMISE ENGINE ============ -->
<div id="ov-deliveryengine" class="ov">
<button class="cbtn" onclick="closeOv()">← Back</button>
<div class="oh" style="background:linear-gradient(155deg,#050e1a 0%,#080808 60%)">
  <div class="otag" style="color:var(--b)">Kafka · Snowflake · dbt · FastAPI · Databricks</div>
  <div class="oname">Real-Time Delivery Promise Engine</div>
  <div class="ohead">Recalculates customer-facing delivery promises as supply-chain events arrive, and serves the current promise through a sub-500ms API — closing the gap batch recomputation leaves open for 12+ hours at a time.</div>
  <div class="omets">
    <div class="omet"><div class="omn" style="color:var(--b)">219ms</div><div class="oml">Served Latency (500ms budget)</div></div>
    <div class="omet"><div class="omn" style="color:var(--gr)">15 min</div><div class="oml">Promise Freshness SLA</div></div>
    <div class="omet"><div class="omn" style="color:var(--g)">10 / 72</div><div class="oml">dbt Models / Schema Tests</div></div>
    <div class="omet"><div class="omn" style="color:var(--o)">61</div><div class="oml">Passing Unit Tests</div></div>
    <div class="omet"><div class="omn" style="color:var(--r)">4</div><div class="oml">Kafka Topics, 6 Partitions Each</div></div>
  </div>
</div>
<div class="obody">
  <div class="osec">
    <div class="ostag">The Problem</div>
    <div class="ostit">A Promise Computed Once at Order Time Has No Way to Hear About What Happens Next</div>
    <div class="otxt"><p>The delivery date shown to a customer is typically computed once, at order time, by a nightly batch job. A carrier delay, a stockout, a warehouse over capacity — none of it reaches the customer-facing promise until the next batch run, often 12+ hours later. At scale, that staleness gap shows up directly in three cost lines.</p></div>
    <div class="rgrid">
      <div class="rcard"><div class="rn" style="color:var(--b)">Cart Abandonment</div><div class="rl">A promise that looks worse than a competitor's at checkout — or turns out wrong after purchase — is a lost or returned order.</div></div>
      <div class="rcard"><div class="rn" style="color:var(--gr)">WISMO Volume</div><div class="rl">"Where is my order" contacts are largely a symptom of the promise diverging from operational reality.</div></div>
      <div class="rcard"><div class="rn" style="color:var(--o)">Trust Erosion</div><div class="rl">Repeat-purchase rate correlates with promise reliability; a broken promise costs more than the order it was attached to.</div></div>
    </div>
  </div>
  <div class="osec">
    <div class="ostag">Architecture</div>
    <div class="ostit">Recalculation Can Lag Minutes — Serving Cannot</div>
    <div class="otxt"><p>The system deliberately separates promise recalculation (runs on a schedule, can lag) from promise serving (runs on every customer request, must be fast) — the reasoning behind that split is documented in <code>docs/architecture.md</code>.</p></div>
    <div class="flow">
      <div class="fstep"><div class="fsn">Ingest</div><div class="fsname">Kafka (4 topics) → Spark Streaming</div></div>
      <div class="farr">→</div>
      <div class="fstep"><div class="fsn">Land</div><div class="fsname">Delta bronze (S3) + Snowflake RAW</div></div>
      <div class="farr">→</div>
      <div class="fstep"><div class="fsn">dbt</div><div class="fsname">staging → intermediate → gold</div></div>
      <div class="farr">→</div>
      <div class="fstep"><div class="fsn">Serve</div><div class="fsname">FastAPI: GET /promise/{order_id}</div></div>
    </div>
  </div>
  <div class="osec">
    <div class="ostag">Promise &amp; Confidence Logic</div>
    <div class="ostit">Priority-Ordered Status, Additive Confidence Penalties</div>
    <table class="ctbl">
      <thead><tr><th>Priority</th><th>Status</th><th>Condition</th></tr></thead>
      <tbody>
        <tr><td>1</td><td>DELIVERED</td><td>Most recent carrier event is "delivered"</td></tr>
        <tr class="hlrow"><td>2</td><td>DELAYED</td><td>Recalculated delivery &gt;2 hours past original promise</td></tr>
        <tr><td>3</td><td>AT_RISK</td><td>Inventory unavailable, warehouse &gt;90% capacity, or carrier event is "delayed"</td></tr>
        <tr class="hlrow"><td>4</td><td>ON_TIME</td><td>None of the above</td></tr>
      </tbody>
    </table>
    <table class="ctbl">
      <thead><tr><th>Confidence Penalty</th><th>Condition</th><th>Max Deduction</th></tr></thead>
      <tbody>
        <tr><td>Inventory unavailable</td><td>Product out of stock at warehouse</td><td>0.30</td></tr>
        <tr class="hlrow"><td>Warehouse strain</td><td>Capacity &gt;80%, scaled to 100%</td><td>0.25</td></tr>
        <tr><td>No carrier signal yet</td><td>Order hasn't been picked up</td><td>0.20</td></tr>
        <tr class="hlrow"><td>Active delay magnitude</td><td>delay_hours / 48, capped at 1</td><td>0.15</td></tr>
      </tbody>
    </table>
    <div class="insight">Confidence starts at 1.0 and subtracts capped, additive penalties — auditable rather than a black-box score, because a support agent needs to answer "why does this look less certain," not just receive a number.</div>
  </div>
  <div class="osec">
    <div class="ostag">Live Evidence</div>
    <div class="ostit">Served Against a Real Snowflake Warehouse — Not Mocked</div>
    <div class="otxt"><p>A real order's recalculated promise: <code>AT_RISK</code>, confidence <code>0.7</code>, risk reason <code>LOW_INVENTORY</code>, 219ms latency against a 500ms budget. The batch endpoint returned all 3 requested orders (spanning DELIVERED, ON_TIME, AT_RISK), 0 not found. dbt ran all 10 models and all 72 schema tests against the live <code>ANALYTICS</code> schema — 3 gold tables: 300 delivery promises, 4 carriers, 6 warehouses.</p></div>
  </div>
  <div class="osec">
    <div class="ostag">Known Limitations</div>
    <div class="ostit">Documented Tradeoffs, Not Hidden Ones</div>
    <div class="insight"><code>risk_reason</code> is single-cause — if inventory is low <em>and</em> the warehouse is over capacity, only the first-matched reason is surfaced. The bronze→Snowflake bridge is a Spark <code>foreachBatch</code> sink, not managed Snowpipe Streaming — a higher-volume deployment would move to it. The Snowflake serving client is a single connection guarded by a lock (correctness-safe, not pooled) and was built for one worker process. All data in this repository is synthetic.</div>
  </div>
  <div class="osec">
    <div class="ostag">Screenshots</div>
    <div class="ostit">Tests · dbt · Live API · Snowflake</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:2px;margin:20px 0">
      <div style="background:var(--m);border:1px solid var(--bd);overflow:hidden">
        <img src="https://raw.githubusercontent.com/SarrangTech/realtime-delivery-promise-engine/main/docs/screenshots/01_pytest_suite.png" alt="Test suite — 61 tests" style="width:100%;display:block;filter:brightness(0.92)" onerror="this.parentElement.innerHTML='<div style=&quot;padding:32px;font-family:DM Mono,monospace;font-size:10px;color:var(--mu);letter-spacing:.1em;text-transform:uppercase&quot;>Test suite screenshot — github.com/SarrangTech/realtime-delivery-promise-engine</div>'">
        <div style="padding:10px 14px;font-family:'DM Mono',monospace;font-size:9px;letter-spacing:.12em;text-transform:uppercase;color:var(--mu)">61 tests — generator, producer, promise logic, API, dbt schema</div>
      </div>
      <div style="background:var(--m);border:1px solid var(--bd);overflow:hidden">
        <img src="https://raw.githubusercontent.com/SarrangTech/realtime-delivery-promise-engine/main/docs/screenshots/04_dbt_parse.png" alt="dbt project graph" style="width:100%;display:block;filter:brightness(0.92)" onerror="this.parentElement.innerHTML='<div style=&quot;padding:32px;font-family:DM Mono,monospace;font-size:10px;color:var(--mu);letter-spacing:.1em;text-transform:uppercase&quot;>dbt screenshot</div>'">
        <div style="padding:10px 14px;font-family:'DM Mono',monospace;font-size:9px;letter-spacing:.12em;text-transform:uppercase;color:var(--mu)">10 models, 4 sources, 72 schema tests, 0 parse errors</div>
      </div>
      <div style="background:var(--m);border:1px solid var(--bd);overflow:hidden">
        <img src="https://raw.githubusercontent.com/SarrangTech/realtime-delivery-promise-engine/main/docs/screenshots/06_live_promise_response.png" alt="Live delivery promise response" style="width:100%;display:block;filter:brightness(0.92)" onerror="this.parentElement.innerHTML='<div style=&quot;padding:32px;font-family:DM Mono,monospace;font-size:10px;color:var(--mu);letter-spacing:.1em;text-transform:uppercase&quot;>Live API screenshot</div>'">
        <div style="padding:10px 14px;font-family:'DM Mono',monospace;font-size:9px;letter-spacing:.12em;text-transform:uppercase;color:var(--mu)">AT_RISK, confidence 0.7, 219ms — live Snowflake connection</div>
      </div>
      <div style="background:var(--m);border:1px solid var(--bd);overflow:hidden">
        <img src="https://raw.githubusercontent.com/SarrangTech/realtime-delivery-promise-engine/main/docs/screenshots/10_gold_delivery_promises_table.png" alt="Snowflake gold table" style="width:100%;display:block;filter:brightness(0.92)" onerror="this.parentElement.innerHTML='<div style=&quot;padding:32px;font-family:DM Mono,monospace;font-size:10px;color:var(--mu);letter-spacing:.1em;text-transform:uppercase&quot;>Snowflake screenshot</div>'">
        <div style="padding:10px 14px;font-family:'DM Mono',monospace;font-size:9px;letter-spacing:.12em;text-transform:uppercase;color:var(--mu)">GOLD_DELIVERY_PROMISES — 300 computed promises, real order IDs</div>
      </div>
    </div>
  </div>
  <div class="osec">
    <div class="ostag">Stack</div><div class="ostit">Built With</div>
    <div class="tools">
      <span class="ttag">Kafka</span>
      <span class="ttag">Spark Structured Streaming</span>
      <span class="ttag">Delta Lake</span>
      <span class="ttag">Snowflake</span>
      <span class="ttag">dbt</span>
      <span class="ttag">FastAPI</span>
      <span class="ttag">Databricks Asset Bundles</span>
      <span class="ttag">pytest</span>
    </div>
    <div class="olinks">
      <a href="https://github.com/SarrangTech/realtime-delivery-promise-engine" class="olink pri" target="_blank">GitHub →</a>
    </div>
  </div>
</div>
</div>

<!-- ============ PRODUCT DOCS AGENT PIPELINE — AWS ============ -->
<div id="ov-docsagent" class="ov">
<button class="cbtn" onclick="closeOv()">← Back</button>
<div class="oh" style="background:linear-gradient(155deg,#120818 0%,#080808 60%)">
  <div class="otag" style="color:var(--p)">Amazon Bedrock · RAG · Medallion Architecture · AWS Lambda</div>
  <div class="oname">Product Docs Agent Pipeline — AWS</div>
  <div class="ohead">End-to-end AWS pipeline ingesting product documentation from GitHub, refining it through bronze/silver/gold, embedding it with Amazon Bedrock, and exposing a sub-500ms semantic search tool an AI agent can call in real time.</div>
  <div class="omets">
    <div class="omet"><div class="omn" style="color:var(--p)">0.87</div><div class="oml">Relevance — Zero Keyword Overlap</div></div>
    <div class="omet"><div class="omn" style="color:var(--b)">178ms</div><div class="oml">Retrieval Latency</div></div>
    <div class="omet"><div class="omn" style="color:var(--gr)">~$0.01</div><div class="oml">Total Cost, Initial Load</div></div>
    <div class="omet"><div class="omn" style="color:var(--o)">33</div><div class="oml">Chunks Embedded</div></div>
    <div class="omet"><div class="omn" style="color:var(--r)">768</div><div class="oml">Embedding Dimensions</div></div>
  </div>
</div>
<div class="obody">
  <div class="osec">
    <div class="ostag">The Problem</div>
    <div class="ostit">An Agent Is Only as Good as the Data It Can Reach the Moment It Answers</div>
    <div class="otxt">
      <p>Documentation lives in GitHub, updated daily, but there is no reliable path from "doc merged to main" to "agent can quote it." Teams either re-index everything on a schedule (slow, expensive) or skip indexing altogether (agent answers from stale or missing context). And keyword search makes retrieval worse — searching "IAM permissions" returns every file containing the phrase, not the one document that actually explains the design decision. Agents need meaning, not matches.</p>
    </div>
  </div>
  <div class="osec">
    <div class="ostag">What This Pipeline Builds</div>
    <div class="ostit">The Agent-Data Flywheel — Doc Merged to Agent-Quotable in Under an Hour</div>
    <div class="flow">
      <div class="fstep"><div class="fsn">Ingest</div><div class="fsname">GitHub docs → S3 bronze, full provenance</div></div>
      <div class="farr">→</div>
      <div class="fstep"><div class="fsn">Refine</div><div class="fsname">Silver: clean, dedupe by content hash</div></div>
      <div class="farr">→</div>
      <div class="fstep"><div class="fsn">Embed</div><div class="fsname">Gold: chunk (2000/200 overlap) → Bedrock Titan V2</div></div>
      <div class="farr">→</div>
      <div class="fstep"><div class="fsn">Serve</div><div class="fsname">Lambda: cosine similarity, top-k, &lt;500ms</div></div>
    </div>
    <table class="ctbl">
      <thead><tr><th>Layer</th><th>Contains</th><th>Why It's Separate</th></tr></thead>
      <tbody>
        <tr><td>Bronze</td><td>Raw markdown, verbatim</td><td>No transformation — reprocess from here if a downstream parser breaks</td></tr>
        <tr class="hlrow"><td>Silver</td><td>One row per document, cleaned</td><td>Frontmatter parsed, code fences stripped, deduped — debug retrieval quality here</td></tr>
        <tr><td>Gold</td><td>One row per chunk + embedding vector</td><td>The only layer the agent touches — a schema contract, versioned carefully</td></tr>
      </tbody>
    </table>
  </div>
  <div class="osec">
    <div class="ostag">Live Demo Results</div>
    <div class="ostit">Three Queries Against the Deployed Lambda — 33 Embedded Chunks</div>
    <table class="ctbl">
      <thead><tr><th>Query</th><th>Top Score</th><th>Latency</th><th>What It Proves</th></tr></thead>
      <tbody>
        <tr><td>"How do I install aws sdk pandas?"</td><td>0.71</td><td>181ms</td><td>Returns the install-command chunk, not the whole README</td></tr>
        <tr class="hlrow"><td>"How does it handle IAM permissions?"</td><td>0.87</td><td>178ms</td><td>Surfaces an internal architecture decision record with almost no word overlap with the query</td></tr>
        <tr><td>"Run at scale with Ray or Modin?"</td><td>0.56</td><td>200ms</td><td>Finds a PyArrow-vs-Pandas ADR a keyword search would never surface</td></tr>
      </tbody>
    </table>
    <div class="insight">Query 2 found an internal engineering design document scored at 0.87 with almost no word overlap with the question — that's the difference between keyword search and semantic retrieval. The pipeline retrieves intent, not terms.</div>
  </div>
  <div class="osec">
    <div class="ostag">Design Decisions</div>
    <div class="ostit">Idempotent, Hash-Gated, and Auditable by Default</div>
    <div class="rgrid">
      <div class="rcard"><div class="rn" style="color:var(--p)">Idempotent S3 Path</div><div class="rl">Commit SHA in the path — re-running at the same commit overwrites, never duplicates.</div></div>
      <div class="rcard"><div class="rn" style="color:var(--b)">Hash-Gated Embedding</div><div class="rl">Gold checks content_hash before calling Bedrock — a typical hourly refresh re-embeds 0–5 chunks, not the full corpus.</div></div>
      <div class="rcard"><div class="rn" style="color:var(--gr)">In-Memory Vector Search</div><div class="rl">33 chunks at 768 dims fit in Lambda memory — no vector DB needed below ~50,000 chunks.</div></div>
    </div>
  </div>
  <div class="osec">
    <div class="ostag">Cost</div>
    <div class="ostit">~$0.01 Initial Load, Under $1/Month at 10,000 Chunks</div>
    <table class="ctbl">
      <thead><tr><th>Resource</th><th>Cost</th></tr></thead>
      <tbody>
        <tr><td>S3 storage (&lt;1MB total)</td><td>~$0.00/month</td></tr>
        <tr class="hlrow"><td>Bedrock Titan Embeddings (33 chunks, initial)</td><td>~$0.01 one-time</td></tr>
        <tr><td>AWS Lambda</td><td>$0.00 (free tier)</td></tr>
        <tr class="hlrow"><td><strong>Total</strong></td><td><strong>~$0.01</strong></td></tr>
      </tbody>
    </table>
  </div>
  <div class="osec">
    <div class="ostag">How to Scale This</div>
    <div class="ostit">Domain-Agnostic — Only the GitHub Repo Pointer Changes</div>
    <div class="otxt">
      <p>Internal knowledge bases, support ticket deflection, compliance/policy search, clinical and research documentation, multi-source corpora — the bronze/silver/gold/retrieval stack transfers unchanged. Any agent framework that can call an HTTP endpoint or AWS Lambda (Claude tool use, OpenAI function calling, LangGraph, LlamaIndex) can consume this pipeline without modification.</p>
    </div>
  </div>
  <div class="osec">
    <div class="ostag">Stack</div><div class="ostit">Built With</div>
    <div class="tools">
      <span class="ttag">Amazon Bedrock Titan Embeddings V2</span>
      <span class="ttag">AWS Lambda</span>
      <span class="ttag">boto3</span>
      <span class="ttag">S3</span>
      <span class="ttag">Python 3.12</span>
      <span class="ttag">GitHub Actions CI</span>
      <span class="ttag">pytest (70% coverage gate)</span>
      <span class="ttag">ruff</span>
    </div>
    <div class="olinks">
      <a href="https://github.com/SarrangTech/product-docs-agent-pipeline-aws" class="olink pri" target="_blank">GitHub →</a>
    </div>
  </div>
</div>
</div>

<!-- ============ CLINICAL TRIAL SUPPLY CHAIN ANOMALY DETECTION (PLACEHOLDER) ============ -->
<div id="ov-clinicaltrial" class="ov">
<button class="cbtn" onclick="closeOv()">← Back</button>
<div class="oh" style="background:linear-gradient(155deg,#1a1206 0%,#080808 60%)">
  <div class="otag" style="color:var(--o)">Supply Chain · Anomaly Detection · In Progress</div>
  <div class="oname">Clinical Trial Supply Chain Anomaly Detection</div>
  <div class="ohead">Early-stage project — the repository is scaffolded (MIT licensed) and the build is actively underway. Full case study coming once the pipeline is live.</div>
  <div class="omets">
    <div class="omet"><div class="omn" style="color:var(--o)">In Progress</div><div class="oml">Status</div></div>
  </div>
</div>
<div class="obody">
  <div class="osec">
    <div class="ostag">Status</div>
    <div class="ostit">Repository Created — Build In Progress</div>
    <div class="otxt"><p>This project targets anomaly detection in clinical trial supply chains — investigational product distribution, temperature excursions in cold-chain logistics, and site-level stockout risk. The repository currently holds only the project scaffolding; check back for the full write-up as the pipeline comes online.</p></div>
  </div>
  <div class="osec">
    <div class="ostag">Stack</div><div class="ostit">Built With</div>
    <div class="olinks">
      <a href="https://github.com/SarrangTech/clinical-trial-supply-chain-anomaly-detection" class="olink pri" target="_blank">GitHub →</a>
    </div>
  </div>
</div>
</div>
"""

if "</body>" in html:
    html = html.replace("</body>", OVERLAYS + "\n</body>", 1)
    print("OVERLAY OK: 4 overlays added", file=sys.stderr)
else:
    print("OVERLAY FAIL: </body> not found", file=sys.stderr)

sys.stdout.reconfigure(encoding='utf-8')
print(html, end="")
