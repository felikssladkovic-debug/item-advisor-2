---
id: method.graph
title: Method Graph
type: generated
status: generated
version: 0.1
links:
  parent: method.index
  children: []
  related:
    - rules.wiki-linking-rules
---

# Method Graph

Generated from YAML front matter. Do not edit graph edges manually.

```mermaid
graph TD
  method_graph["method.graph<br/>Method Graph"]
  method_index["method.index<br/>Method Index"]
  prompts_01_bootstrap_project_prompt["prompts.01-bootstrap-project.prompt<br/>Bootstrap Project Prompt"]
  rules_change_policy["rules.change-policy<br/>Change Policy"]
  rules_consistency_policy["rules.consistency-policy<br/>Consistency Policy"]
  rules_human_llm_codex_roles["rules.human-llm-codex-roles<br/>Human / LLM / Codex Roles"]
  rules_layers_and_flow["rules.layers-and-flow<br/>Layers and Flow"]
  rules_naming_rules["rules.naming-rules<br/>Naming Rules"]
  rules_project_version_binding["rules.project-version-binding<br/>Project Version Binding"]
  rules_repository_model["rules.repository-model<br/>Repository Model"]
  rules_review_policy["rules.review-policy<br/>Review Policy"]
  rules_traceability_policy["rules.traceability-policy<br/>Traceability Policy"]
  rules_wiki_linking_rules["rules.wiki-linking-rules<br/>Wiki Linking Rules"]
  rules_workflow_overview["rules.workflow-overview<br/>Workflow Overview"]
  starting_foundation_change_requests_index["starting-foundation.change-requests.index<br/>Starting Foundation / Change Requests"]
  starting_foundation_decisions_index["starting-foundation.decisions.index<br/>Starting Foundation / Decisions"]
  starting_foundation_ideas_index["starting-foundation.ideas.index<br/>Starting Foundation / Ideas"]
  starting_foundation_index["starting-foundation.index<br/>Starting Foundation"]
  starting_foundation_spec_index["starting-foundation.spec.index<br/>Starting Foundation / Spec"]
  templates_business_idea_template["templates.business-idea-template<br/>Business Idea Template"]
  templates_change_request_template["templates.change-request-template<br/>Change Request Template"]
  templates_decision_log_template["templates.decision-log-template<br/>Decision Log Template"]
  templates_spec_template["templates.spec-template<br/>Specification Template"]

  method_index --> starting_foundation_index
  method_index --> rules_workflow_overview
  method_index --> rules_wiki_linking_rules
  method_index --> rules_naming_rules
  method_index --> rules_project_version_binding
  method_index --> templates_business_idea_template
  method_index --> templates_spec_template
  method_index --> templates_decision_log_template
  method_index --> templates_change_request_template
  method_index --> prompts_01_bootstrap_project_prompt
  method_index -. related .-> method_graph
  method_index --> prompts_01_bootstrap_project_prompt
  prompts_01_bootstrap_project_prompt -. related .-> rules_workflow_overview
  prompts_01_bootstrap_project_prompt -. related .-> rules_wiki_linking_rules
  rules_workflow_overview --> rules_change_policy
  rules_change_policy -. related .-> templates_change_request_template
  rules_change_policy -. related .-> rules_traceability_policy
  method_index --> rules_consistency_policy
  rules_consistency_policy -. related .-> rules_traceability_policy
  rules_consistency_policy -. related .-> rules_review_policy
  rules_workflow_overview --> rules_human_llm_codex_roles
  rules_human_llm_codex_roles -. related .-> rules_traceability_policy
  rules_human_llm_codex_roles -. related .-> rules_review_policy
  rules_workflow_overview --> rules_layers_and_flow
  rules_layers_and_flow -. related .-> rules_traceability_policy
  method_index --> rules_naming_rules
  rules_naming_rules -. related .-> rules_wiki_linking_rules
  method_index --> rules_project_version_binding
  rules_project_version_binding -. related .-> rules_traceability_policy
  method_index --> rules_repository_model
  rules_repository_model -. related .-> rules_workflow_overview
  rules_workflow_overview --> rules_review_policy
  rules_review_policy -. related .-> rules_human_llm_codex_roles
  rules_review_policy -. related .-> rules_traceability_policy
  rules_workflow_overview --> rules_traceability_policy
  rules_traceability_policy -. related .-> rules_consistency_policy
  rules_traceability_policy -. related .-> templates_spec_template
  rules_traceability_policy -. related .-> templates_decision_log_template
  method_index --> rules_wiki_linking_rules
  rules_wiki_linking_rules -. related .-> method_graph
  method_index --> rules_workflow_overview
  rules_workflow_overview --> rules_human_llm_codex_roles
  rules_workflow_overview --> rules_traceability_policy
  rules_workflow_overview --> rules_change_policy
  rules_workflow_overview --> rules_review_policy
  rules_workflow_overview --> rules_layers_and_flow
  rules_workflow_overview -. related .-> rules_repository_model
  starting_foundation_index --> starting_foundation_change_requests_index
  starting_foundation_change_requests_index -. related .-> templates_change_request_template
  starting_foundation_change_requests_index -. related .-> rules_change_policy
  starting_foundation_change_requests_index -. related .-> rules_project_version_binding
  starting_foundation_index --> starting_foundation_decisions_index
  starting_foundation_decisions_index -. related .-> templates_decision_log_template
  starting_foundation_decisions_index -. related .-> rules_change_policy
  starting_foundation_decisions_index -. related .-> rules_review_policy
  starting_foundation_index --> starting_foundation_ideas_index
  starting_foundation_ideas_index -. related .-> templates_business_idea_template
  starting_foundation_ideas_index -. related .-> rules_traceability_policy
  method_index --> starting_foundation_index
  starting_foundation_index --> starting_foundation_ideas_index
  starting_foundation_index --> starting_foundation_spec_index
  starting_foundation_index --> starting_foundation_decisions_index
  starting_foundation_index --> starting_foundation_change_requests_index
  starting_foundation_index -. related .-> rules_workflow_overview
  starting_foundation_index -. related .-> rules_repository_model
  starting_foundation_index -. related .-> prompts_01_bootstrap_project_prompt
  starting_foundation_index --> starting_foundation_spec_index
  starting_foundation_spec_index -. related .-> templates_spec_template
  starting_foundation_spec_index -. related .-> rules_traceability_policy
  starting_foundation_spec_index -. related .-> rules_consistency_policy
  method_index --> templates_business_idea_template
  templates_business_idea_template -. related .-> templates_spec_template
  method_index --> templates_change_request_template
  templates_change_request_template -. related .-> rules_change_policy
  method_index --> templates_decision_log_template
  templates_decision_log_template -. related .-> rules_traceability_policy
  method_index --> templates_spec_template
  templates_spec_template -. related .-> templates_business_idea_template
  templates_spec_template -. related .-> rules_traceability_policy
```
