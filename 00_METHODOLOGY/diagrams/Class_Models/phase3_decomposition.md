# Phase 3 — Decomposition

**Version:** 2.0 — UC-Centric Iterative Decomposition — 05/04/2026
**Status:** ✅ Updated with UseCaseRelationship, VariabilityType, multi-level support

## Entities

### Bridge from Phase 2
- RulesCatalog, AbstractRule

### Bridge from Phase 1
- Stakeholder, BusinessGoal

### New in Phase 3 Decomposition
- UseCase, UseCaseRelationship, FunctionalNode, ComplianceGate, AssetContext

```mermaid
classDiagram

    %% ── BRIDGE FROM PREVIOUS PHASES ─────────────────────────────────

    class RulesCatalog {
        +String catalogId
        +Date versionDate
        +String scope
    }

    class AbstractRule {
        +String ruleId
        +String description
        +String targetSubDomain
        +Float normativeIntensity
        +RuleSource sourceType
    }

    class Stakeholder {
        +String stakeholderId
        +String name
        +String role
    }
    note for Stakeholder "from Phase 1"

    class BusinessGoal {
        +String goalId
        +String description
        +String priority
        +String strategicAlignment
    }

    %% ── NEW IN PHASE 3 DECOMPOSITION ────────────────────────────────

    class UseCase {
        +String useCaseId
        +String name
        +String description
        +DecompositionLevel level
        +String[] actors
        +String[] ruleMappings
        +Priority priority
        +String sla
        +VariabilityType variabilityType
    }

    class UseCaseRelationship {
        +String relationshipId
        +RelationshipType type
        +String stereotype
        +String sourceUseCaseId
        +String targetUseCaseId
        +String rationale
    }

    class FunctionalNode {
        +String nodeId
        +String name
        +String description
        +Track track
        +DecompositionLevel level
        +String verificationMethod
        +String sourceUseCaseId
    }

    class ComplianceGate {
        +String gateId
        +Date evaluationDate
        +GateStatus status
        +String[] gapsIdentified
    }

    class AssetContext {
        +String assetId
        +String assetType
        +String classification
        +String[] regulatoryConstraints
    }

    %% ── ENUMERATIONS ─────────────────────────────────────────────────

    class DecompositionLevel {
        <<enumeration>>
        L0_BOUNDARY
        L1_PRIMARY
        L2_SUBFLOW
        LN_ATOMIC
    }

    class RelationshipType {
        <<enumeration>>
        INCLUDE
        REFINE
        EXTEND
    }

    class VariabilityType {
        <<enumeration>>
        NONE
        ALTERNATIVE
        SPECIALIZATION
        OPTION
    }

    class GateStatus {
        <<enumeration>>
        PASS
        GAP_DETECTED
        PENDING
    }

    class RuleSource {
        <<enumeration>>
        REGULATORY
        BEST_PRACTICE
        HYBRID
    }

    class Track {
        <<enumeration>>
        TECHNOLOGY
        PROCESS
        CAPABILITY_SUBREQ
    }

    class Priority {
        <<enumeration>>
        CRITICAL
        HIGH
        MEDIUM
        LOW
    }

    %% ── RELATIONSHIPS ────────────────────────────────────────────────

    RulesCatalog "1" *-- "1..*" AbstractRule : aggregates
    Stakeholder "1..*" --> "1..*" UseCase : participates in
    BusinessGoal "1..*" --> "1..*" UseCase : motivates

    UseCase "1" --> "0..*" UseCaseRelationship : participates in
    UseCaseRelationship "1" --> "1" UseCase : source
    UseCaseRelationship "1" --> "1" UseCase : target

    UseCase "1..*" --> "1..*" FunctionalNode : derives
    FunctionalNode "0..1" --> "1" UseCase : sourced from

    AbstractRule "1..*" --> "1..*" FunctionalNode : constrains
    FunctionalNode "1" *-- "0..*" ComplianceGate : validated by

    ComplianceGate "1" --> "1..*" AbstractRule : checks against
    ComplianceGate "0..*" --> "0..*" FunctionalNode : generates

    AssetContext "1..*" --> "0..*" ComplianceGate : informs
    AssetContext "1..*" --> "1..*" FunctionalNode : protected by

    FunctionalNode ..> Track : uses
    FunctionalNode ..> DecompositionLevel : uses
    ComplianceGate ..> GateStatus : uses
    AbstractRule ..> RuleSource : uses
    UseCase ..> DecompositionLevel : uses
    UseCase ..> VariabilityType : uses
    UseCaseRelationship ..> RelationshipType : uses
    FunctionalNode ..> Priority : uses
    UseCase ..> Priority : uses
```

## OCL Constraints

### Coexistence Constraint
A use case CANNOT have both `«include»` and `«refine»` relationships to the same target use case.

```ocl
context UseCase inv:
    if self.outgoingRelationships->exists(r | r.type = RelationshipType::INCLUDE)
        and self.outgoingRelationships->exists(r | r.type = RelationshipType::REFINE)
    then
        self.outgoingRelationships->select(r | r.type = RelationshipType::INCLUDE).target
            ->intersection(
                self.outgoingRelationships->select(r | r.type = RelationshipType::REFINE).target
            )->isEmpty()
    endif
```

### Multiple Refines Constraint
A refined use case MUST be refined by ≥2 refining use cases (unless it's a leaf).

```ocl
context UseCase inv:
    let refines : Set(UseCaseRelationship) = 
        self.incomingRelationships->select(r | r.type = RelationshipType::REFINE) in
    if refines->size() >= 2
    then
        let includes : Integer = refines->iterate(
            nextElement : UseCaseRelationship; 
            accumulator : Integer = 0 | 
            accumulator + nextElement.source.outgoingRelationships
                ->select(r | r.type = RelationshipType::INCLUDE)->size()
        ) in
        refines->size() - 1 = includes
    endif
```

### Level Consistency
`«refine»` relationships MUST go from higher to lower abstraction level.

```ocl
context UseCaseRelationship inv:
    if self.type = RelationshipType::REFINE
    then
        self.source.level.ordinal() < self.target.level.ordinal()
    endif
```

### Orphan Prevention
Every use case at Level ≥1 MUST have at least one incoming relationship (`«include»` or `«refine»`).

```ocl
context UseCase inv:
    if self.level <> DecompositionLevel::L0_BOUNDARY
    then
        self.incomingRelationships->size() >= 1
    endif
```
