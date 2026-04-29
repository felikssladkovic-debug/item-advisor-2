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
  rules_ideas_to_spec_mapping["rules.ideas-to-spec-mapping<br/>Ideas to Spec Mapping Contract"]
  rules_layers_and_flow["rules.layers-and-flow<br/>Layers and Flow"]
  rules_naming_rules["rules.naming-rules<br/>Naming Rules"]
  rules_project_lifecycle["rules.project-lifecycle<br/>Project Lifecycle"]
  rules_project_version_binding["rules.project-version-binding<br/>Project Version Binding"]
  rules_repository_model["rules.repository-model<br/>Repository Model"]
  rules_review_policy["rules.review-policy<br/>Review Policy"]
  rules_traceability_policy["rules.traceability-policy<br/>Traceability Policy"]
  rules_wiki_linking_rules["rules.wiki-linking-rules<br/>Wiki Linking Rules"]
  rules_workflow_overview["rules.workflow-overview<br/>Workflow Overview"]
  starting_foundation_change_requests_index["starting-foundation.change-requests.index<br/>Starting Foundation / Change Requests"]
  starting_foundation_checks_acceptance_checklist["starting-foundation.checks.acceptance-checklist<br/>Acceptance Checklist"]
  starting_foundation_checks_index["starting-foundation.checks.index<br/>Starting Foundation / Checks"]
  starting_foundation_decisions_0001_foundation_scope["starting-foundation.decisions.0001-foundation-scope<br/>Foundation Scope: Site, Admin, Shared Database"]
  starting_foundation_decisions_index["starting-foundation.decisions.index<br/>Starting Foundation / Decisions"]
  starting_foundation_ideas_000_project_intent["starting-foundation.ideas.000-project-intent<br/>Project Intent"]
  starting_foundation_ideas_accepted_001_application_shape["starting-foundation.ideas.accepted.001-application-shape<br/>Application Shape"]
  starting_foundation_ideas_accepted_002_database["starting-foundation.ideas.accepted.002-database<br/>Shared Database"]
  starting_foundation_ideas_accepted_003_site_behavior["starting-foundation.ideas.accepted.003-site-behavior<br/>Site Behavior"]
  starting_foundation_ideas_accepted_004_admin_behavior["starting-foundation.ideas.accepted.004-admin-behavior<br/>Admin Behavior"]
  starting_foundation_ideas_accepted_005_admin_scope["starting-foundation.ideas.accepted.005-admin-scope<br/>Admin Scope"]
  starting_foundation_ideas_accepted_index["starting-foundation.ideas.accepted.index<br/>Accepted Ideas Index"]
  starting_foundation_ideas_archive_README["starting-foundation.ideas.archive.README<br/>Ideas Archive"]
  starting_foundation_ideas_boundaries_001_out_of_scope["starting-foundation.ideas.boundaries.001-out-of-scope<br/>Out of Scope"]
  starting_foundation_ideas_boundaries_index["starting-foundation.ideas.boundaries.index<br/>Boundaries Index"]
  starting_foundation_ideas_inbox_README["starting-foundation.ideas.inbox.README<br/>Ideas Inbox"]
  starting_foundation_ideas_index["starting-foundation.ideas.index<br/>Starting Foundation / Ideas"]
  starting_foundation_index["starting-foundation.index<br/>Starting Foundation / Site Admin DB"]
  starting_foundation_prompts_01_generate_code_from_spec_prompt["starting-foundation.prompts.01-generate-code-from-spec.prompt<br/>Generate Code From Spec Prompt"]
  starting_foundation_prompts_02_incremental_code_update_prompt["starting-foundation.prompts.02-incremental-code-update.prompt<br/>Incremental Code Update Prompt"]
  starting_foundation_prompts_03_validate_code_against_spec_prompt["starting-foundation.prompts.03-validate-code-against-spec.prompt<br/>Validate Code Against Spec Prompt"]
  starting_foundation_prompts_04_run_acceptance_checks_prompt["starting-foundation.prompts.04-run-acceptance-checks.prompt<br/>Run Acceptance Checks Prompt"]
  starting_foundation_prompts_index["starting-foundation.prompts.index<br/>Starting Foundation / Project Prompts"]
  starting_foundation_spec_00_overview["starting-foundation.spec.00-overview<br/>Overview"]
  starting_foundation_spec_01_architecture["starting-foundation.spec.01-architecture<br/>Architecture"]
  starting_foundation_spec_02_applications["starting-foundation.spec.02-applications<br/>Applications"]
  starting_foundation_spec_03_database["starting-foundation.spec.03-database<br/>Database"]
  starting_foundation_spec_04_runtime_modes["starting-foundation.spec.04-runtime-modes<br/>Runtime Modes"]
  starting_foundation_spec_05_acceptance_criteria["starting-foundation.spec.05-acceptance-criteria<br/>Acceptance Criteria"]
  starting_foundation_spec_06_non_goals["starting-foundation.spec.06-non-goals<br/>Non-goals"]
  starting_foundation_spec_index["starting-foundation.spec.index<br/>Starting Foundation / Spec"]
  templates_business_idea_template["templates.business-idea-template<br/>Business Idea Template"]
  templates_change_request_template["templates.change-request-template<br/>Change Request Template"]
  templates_decision_log_template["templates.decision-log-template<br/>Decision Log Template"]
  templates_spec_template["templates.spec-template<br/>Specification Template"]

  method_index --> starting_foundation_index
  method_index --> rules_workflow_overview
  method_index --> rules_project_lifecycle
  method_index --> rules_ideas_to_spec_mapping
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
  rules_human_llm_codex_roles -. related .-> rules_project_lifecycle
  rules_human_llm_codex_roles -. related .-> rules_traceability_policy
  rules_human_llm_codex_roles -. related .-> rules_review_policy
  method_index --> rules_ideas_to_spec_mapping
  rules_ideas_to_spec_mapping -. related .-> rules_workflow_overview
  rules_ideas_to_spec_mapping -. related .-> rules_project_lifecycle
  rules_ideas_to_spec_mapping -. related .-> rules_traceability_policy
  rules_ideas_to_spec_mapping -. related .-> rules_consistency_policy
  rules_workflow_overview --> rules_layers_and_flow
  rules_layers_and_flow -. related .-> rules_traceability_policy
  method_index --> rules_naming_rules
  rules_naming_rules -. related .-> rules_wiki_linking_rules
  rules_workflow_overview --> rules_project_lifecycle
  rules_project_lifecycle -. related .-> rules_layers_and_flow
  rules_project_lifecycle -. related .-> rules_human_llm_codex_roles
  rules_project_lifecycle -. related .-> rules_ideas_to_spec_mapping
  rules_project_lifecycle -. related .-> rules_traceability_policy
  rules_project_lifecycle -. related .-> rules_change_policy
  rules_project_lifecycle -. related .-> rules_review_policy
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
  rules_workflow_overview --> rules_project_lifecycle
  rules_workflow_overview --> rules_human_llm_codex_roles
  rules_workflow_overview --> rules_ideas_to_spec_mapping
  rules_workflow_overview --> rules_traceability_policy
  rules_workflow_overview --> rules_change_policy
  rules_workflow_overview --> rules_review_policy
  rules_workflow_overview --> rules_layers_and_flow
  rules_workflow_overview -. related .-> rules_repository_model
  starting_foundation_index --> starting_foundation_change_requests_index
  starting_foundation_change_requests_index -. related .-> templates_change_request_template
  starting_foundation_change_requests_index -. related .-> rules_change_policy
  starting_foundation_change_requests_index -. related .-> rules_project_version_binding
  starting_foundation_checks_index --> starting_foundation_checks_acceptance_checklist
  starting_foundation_checks_acceptance_checklist -. related .-> rules_project_lifecycle
  starting_foundation_checks_acceptance_checklist -. related .-> starting_foundation_spec_05_acceptance_criteria
  starting_foundation_index --> starting_foundation_checks_index
  starting_foundation_checks_index --> starting_foundation_checks_acceptance_checklist
  starting_foundation_checks_index -. related .-> rules_project_lifecycle
  starting_foundation_checks_index -. related .-> starting_foundation_spec_05_acceptance_criteria
  starting_foundation_decisions_index --> starting_foundation_decisions_0001_foundation_scope
  starting_foundation_decisions_0001_foundation_scope -. related .-> starting_foundation_ideas_accepted_001_application_shape
  starting_foundation_decisions_0001_foundation_scope -. related .-> starting_foundation_spec_01_architecture
  starting_foundation_index --> starting_foundation_decisions_index
  starting_foundation_decisions_index --> starting_foundation_decisions_0001_foundation_scope
  starting_foundation_decisions_index -. related .-> templates_decision_log_template
  starting_foundation_decisions_index -. related .-> rules_change_policy
  starting_foundation_decisions_index -. related .-> rules_review_policy
  starting_foundation_ideas_index --> starting_foundation_ideas_000_project_intent
  starting_foundation_ideas_000_project_intent -. related .-> starting_foundation_spec_00_overview
  starting_foundation_ideas_000_project_intent -. related .-> starting_foundation_spec_01_architecture
  starting_foundation_ideas_accepted_index --> starting_foundation_ideas_accepted_001_application_shape
  starting_foundation_ideas_accepted_001_application_shape -. related .-> starting_foundation_spec_01_architecture
  starting_foundation_ideas_accepted_index --> starting_foundation_ideas_accepted_002_database
  starting_foundation_ideas_accepted_002_database -. related .-> starting_foundation_spec_03_database
  starting_foundation_ideas_accepted_index --> starting_foundation_ideas_accepted_003_site_behavior
  starting_foundation_ideas_accepted_003_site_behavior -. related .-> starting_foundation_spec_02_applications
  starting_foundation_ideas_accepted_index --> starting_foundation_ideas_accepted_004_admin_behavior
  starting_foundation_ideas_accepted_004_admin_behavior -. related .-> starting_foundation_spec_02_applications
  starting_foundation_ideas_accepted_index --> starting_foundation_ideas_accepted_005_admin_scope
  starting_foundation_ideas_accepted_005_admin_scope -. related .-> starting_foundation_spec_02_applications
  starting_foundation_ideas_accepted_005_admin_scope -. related .-> starting_foundation_spec_06_non_goals
  starting_foundation_ideas_index --> starting_foundation_ideas_accepted_index
  starting_foundation_ideas_accepted_index --> starting_foundation_ideas_accepted_001_application_shape
  starting_foundation_ideas_accepted_index --> starting_foundation_ideas_accepted_002_database
  starting_foundation_ideas_accepted_index --> starting_foundation_ideas_accepted_003_site_behavior
  starting_foundation_ideas_accepted_index --> starting_foundation_ideas_accepted_004_admin_behavior
  starting_foundation_ideas_accepted_index --> starting_foundation_ideas_accepted_005_admin_scope
  starting_foundation_ideas_accepted_index -. related .-> rules_ideas_to_spec_mapping
  starting_foundation_ideas_index --> starting_foundation_ideas_archive_README
  starting_foundation_ideas_archive_README -. related .-> rules_ideas_to_spec_mapping
  starting_foundation_ideas_boundaries_index --> starting_foundation_ideas_boundaries_001_out_of_scope
  starting_foundation_ideas_boundaries_001_out_of_scope -. related .-> starting_foundation_spec_06_non_goals
  starting_foundation_ideas_index --> starting_foundation_ideas_boundaries_index
  starting_foundation_ideas_boundaries_index --> starting_foundation_ideas_boundaries_001_out_of_scope
  starting_foundation_ideas_boundaries_index -. related .-> rules_ideas_to_spec_mapping
  starting_foundation_ideas_index --> starting_foundation_ideas_inbox_README
  starting_foundation_ideas_inbox_README -. related .-> rules_ideas_to_spec_mapping
  starting_foundation_index --> starting_foundation_ideas_index
  starting_foundation_ideas_index --> starting_foundation_ideas_000_project_intent
  starting_foundation_ideas_index --> starting_foundation_ideas_accepted_index
  starting_foundation_ideas_index --> starting_foundation_ideas_boundaries_index
  starting_foundation_ideas_index --> starting_foundation_ideas_inbox_README
  starting_foundation_ideas_index --> starting_foundation_ideas_archive_README
  starting_foundation_ideas_index -. related .-> templates_business_idea_template
  starting_foundation_ideas_index -. related .-> rules_traceability_policy
  starting_foundation_ideas_index -. related .-> rules_ideas_to_spec_mapping
  method_index --> starting_foundation_index
  starting_foundation_index --> starting_foundation_ideas_index
  starting_foundation_index --> starting_foundation_spec_index
  starting_foundation_index --> starting_foundation_decisions_index
  starting_foundation_index --> starting_foundation_change_requests_index
  starting_foundation_index --> starting_foundation_prompts_index
  starting_foundation_index --> starting_foundation_checks_index
  starting_foundation_index -. related .-> rules_workflow_overview
  starting_foundation_index -. related .-> rules_project_lifecycle
  starting_foundation_index -. related .-> rules_repository_model
  starting_foundation_index -. related .-> prompts_01_bootstrap_project_prompt
  starting_foundation_prompts_index --> starting_foundation_prompts_01_generate_code_from_spec_prompt
  starting_foundation_prompts_01_generate_code_from_spec_prompt -. related .-> rules_project_lifecycle
  starting_foundation_prompts_01_generate_code_from_spec_prompt -. related .-> rules_ideas_to_spec_mapping
  starting_foundation_prompts_01_generate_code_from_spec_prompt -. related .-> starting_foundation_spec_index
  starting_foundation_prompts_01_generate_code_from_spec_prompt -. related .-> starting_foundation_checks_acceptance_checklist
  starting_foundation_prompts_index --> starting_foundation_prompts_02_incremental_code_update_prompt
  starting_foundation_prompts_02_incremental_code_update_prompt -. related .-> rules_project_lifecycle
  starting_foundation_prompts_02_incremental_code_update_prompt -. related .-> rules_ideas_to_spec_mapping
  starting_foundation_prompts_02_incremental_code_update_prompt -. related .-> starting_foundation_spec_index
  starting_foundation_prompts_index --> starting_foundation_prompts_03_validate_code_against_spec_prompt
  starting_foundation_prompts_03_validate_code_against_spec_prompt -. related .-> rules_project_lifecycle
  starting_foundation_prompts_03_validate_code_against_spec_prompt -. related .-> rules_ideas_to_spec_mapping
  starting_foundation_prompts_03_validate_code_against_spec_prompt -. related .-> starting_foundation_spec_index
  starting_foundation_prompts_index --> starting_foundation_prompts_04_run_acceptance_checks_prompt
  starting_foundation_prompts_04_run_acceptance_checks_prompt -. related .-> rules_project_lifecycle
  starting_foundation_prompts_04_run_acceptance_checks_prompt -. related .-> starting_foundation_checks_acceptance_checklist
  starting_foundation_index --> starting_foundation_prompts_index
  starting_foundation_prompts_index --> starting_foundation_prompts_01_generate_code_from_spec_prompt
  starting_foundation_prompts_index --> starting_foundation_prompts_02_incremental_code_update_prompt
  starting_foundation_prompts_index --> starting_foundation_prompts_03_validate_code_against_spec_prompt
  starting_foundation_prompts_index --> starting_foundation_prompts_04_run_acceptance_checks_prompt
  starting_foundation_prompts_index -. related .-> rules_project_lifecycle
  starting_foundation_prompts_index -. related .-> rules_ideas_to_spec_mapping
  starting_foundation_spec_index --> starting_foundation_spec_00_overview
  starting_foundation_spec_00_overview -. related .-> starting_foundation_ideas_000_project_intent
  starting_foundation_spec_00_overview -. related .-> starting_foundation_spec_01_architecture
  starting_foundation_spec_index --> starting_foundation_spec_01_architecture
  starting_foundation_spec_01_architecture -. related .-> starting_foundation_ideas_000_project_intent
  starting_foundation_spec_01_architecture -. related .-> starting_foundation_ideas_accepted_001_application_shape
  starting_foundation_spec_01_architecture -. related .-> starting_foundation_decisions_0001_foundation_scope
  starting_foundation_spec_01_architecture -. related .-> starting_foundation_spec_02_applications
  starting_foundation_spec_01_architecture -. related .-> starting_foundation_spec_03_database
  starting_foundation_spec_index --> starting_foundation_spec_02_applications
  starting_foundation_spec_02_applications -. related .-> starting_foundation_ideas_accepted_003_site_behavior
  starting_foundation_spec_02_applications -. related .-> starting_foundation_ideas_accepted_004_admin_behavior
  starting_foundation_spec_02_applications -. related .-> starting_foundation_ideas_accepted_005_admin_scope
  starting_foundation_spec_02_applications -. related .-> starting_foundation_spec_01_architecture
  starting_foundation_spec_02_applications -. related .-> starting_foundation_spec_05_acceptance_criteria
  starting_foundation_spec_index --> starting_foundation_spec_03_database
  starting_foundation_spec_03_database -. related .-> starting_foundation_ideas_accepted_002_database
  starting_foundation_spec_03_database -. related .-> starting_foundation_spec_01_architecture
  starting_foundation_spec_03_database -. related .-> starting_foundation_spec_05_acceptance_criteria
  starting_foundation_spec_index --> starting_foundation_spec_04_runtime_modes
  starting_foundation_spec_04_runtime_modes -. related .-> starting_foundation_spec_05_acceptance_criteria
  starting_foundation_spec_index --> starting_foundation_spec_05_acceptance_criteria
  starting_foundation_spec_05_acceptance_criteria -. related .-> starting_foundation_ideas_boundaries_001_out_of_scope
  starting_foundation_spec_05_acceptance_criteria -. related .-> starting_foundation_spec_02_applications
  starting_foundation_spec_05_acceptance_criteria -. related .-> starting_foundation_spec_03_database
  starting_foundation_spec_05_acceptance_criteria -. related .-> starting_foundation_spec_04_runtime_modes
  starting_foundation_spec_05_acceptance_criteria -. related .-> starting_foundation_checks_acceptance_checklist
  starting_foundation_spec_index --> starting_foundation_spec_06_non_goals
  starting_foundation_spec_06_non_goals -. related .-> starting_foundation_ideas_boundaries_001_out_of_scope
  starting_foundation_index --> starting_foundation_spec_index
  starting_foundation_spec_index --> starting_foundation_spec_00_overview
  starting_foundation_spec_index --> starting_foundation_spec_01_architecture
  starting_foundation_spec_index --> starting_foundation_spec_02_applications
  starting_foundation_spec_index --> starting_foundation_spec_03_database
  starting_foundation_spec_index --> starting_foundation_spec_04_runtime_modes
  starting_foundation_spec_index --> starting_foundation_spec_05_acceptance_criteria
  starting_foundation_spec_index --> starting_foundation_spec_06_non_goals
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
