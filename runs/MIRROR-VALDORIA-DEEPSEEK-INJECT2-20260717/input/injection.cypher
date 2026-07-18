// P2 INJECT2 — graph injection of 8 Valdoria absurdity classes (gate G3, replicate)
// graph_id: db1699ce-b54f-4643-a91d-61e51315fa2a | Neo4j HTTP API at Enter-Env-Setup gate | ts 2026-07-17T15:09:00Z
MATCH (v:Entity {graph_id:$g, name:'Valdoria'})
UNWIND $facts AS f
CREATE (n:Entity:InjectedAbsurdity {uuid: randomUUID(), name: f.name, name_lower: toLower(f.name), graph_id: $g, summary: f.summary, created_at: $ts, injected: true})
CREATE (v)-[:HAS_ABSURD_ATTRIBUTE {injected:true}]->(n) RETURN count(n) AS created;
// Same 8 classes A1-A8 as INJECT1. RESULT: created=8, 0 errors. Graph 11n/5e -> 19n/13e.
// NOTE: before-graph had distinct 'current monarch' node (11th) -> this run has both valdoria_664 and current_monarch_781 agents.
