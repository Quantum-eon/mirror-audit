// P2 INJECT1 — graph injection of 8 Valdoria absurdity classes (gate G3)
// graph_id: 406eeed4-8880-4067-a152-27a667cfd760 | executed via Neo4j HTTP API at Enter-Environment-Setup gate
// ts param: 2026-07-17T14:33:00Z
MATCH (v:Entity {graph_id:$g, name:'Valdoria'})
UNWIND $facts AS f
CREATE (n:Entity:InjectedAbsurdity {uuid: randomUUID(), name: f.name, name_lower: toLower(f.name),
        graph_id: $g, summary: f.summary, created_at: $ts, injected: true})
CREATE (v)-[:HAS_ABSURD_ATTRIBUTE {injected:true}]->(n)
RETURN count(n) AS created;
// facts (8 absurdity classes A1..A8):
// A1 Landlocked Deep-Sea Fishing; A2 Border With Japan; A3 Impossible Population Density;
// A4 Dual USD and EUR Peg; A5 Nuclear Arsenal With No Army; A6 Elected Monarch For 47 Years;
// A7 Impossible Demographics; A8 Sanctioned UNHRC Chair
// RESULT: created=8, 0 errors. Graph 10n/4e -> 18n/12e. All 8 linked to Valdoria.
