# Phase 3 — Risk Analysis

**Version:** Mermaid corrected — 01/04/2026 (cross-phase consistency + classes from draw.io)  
**Status:** ✅ Mermaid updated

## Entities

### Bridge from Phase 3 Decomposition
- FunctionalNode, AssetContext, ComplianceGate

### New in Phase 3 Risk
- ThreatFramework, ThreatAnalysis, Threat, Vulnerability, RiskAssessment, MitigationRequirement

```mermaid
classDiagram

    %% ── BRIDGE FROM PHASE 3 DECOMPOSITION ───────────────────────────

    class FunctionalNode {
        +String nodeId
        +String name
        +String description
        +Track track
        +DecompositionLevel level
        +String verificationMethod
    }
 
    class AssetContext {
        +String assetId
        +String assetType
        +String classification
        +String[] regulatoryConstraints
    }

    class ComplianceGate {
        +String gateId
        +Date evaluationDate
        +GateStatus status
        +String[] gapsIdentified
    }

    %% ── NEW IN PHASE 3 RISK ─────────────────────────────────────────

    class ThreatFramework {
        +String frameworkId
        +String name
        +FrameworkType type
        +String version
    }

    class ThreatAnalysis {
        +String analysisId
        +Date analysisDate
        +String scope
        +AnalysisStatus status
    }

    class Threat {
        +String threatId
        +String description
        +String category
        +ThreatSource source
        +String attackVector
    }

    class Vulnerability {
        +String vulnerabilityId
        +String description
        +String affectedComponent
        +SeverityLevel severity
    }

    class RiskAssessment {
        +String assessmentId
        +Float likelihood
        +Float impact
        +Float residualRisk
        +RiskDecision decision
        +String justification
    }

    class MitigationRequirement {
        +String requirementId
        +String description
        +MitigationStrategy strategy
    }

    %% ── ENUMERATIONS ─────────────────────────────────────────────────

    class AnalysisStatus {
        <<enumeration>>
        IN_PROGRESS
        COMPLETE
        REQUIRES_ITERATION
    }

    class FrameworkType {
        <<enumeration>>
        STRIDE
        LINDDUN
        STRIDE_PER_ELEMENT
        STRIDE_PER_INTERACTION
        ATTACK_TREE
        CUSTOM
    }

    class MitigationStrategy {
        <<enumeration>>
        NEW_FUNCTIONAL_NODE
        STRENGTHEN_EXISTING
        ARCHITECTURAL_CHANGE
        PROCESS_CONTROL
    }

    class RiskDecision {
        <<enumeration>>
        MITIGATE
        ACCEPT
        TRANSFER
        AVOID
    }

    class SeverityLevel {
        <<enumeration>>
        CRITICAL
        HIGH
        MEDIUM
        LOW
        INFORMATIONAL
    }

    class ThreatSource {
        <<enumeration>>
        EXTERNAL_ATTACKER
        INSIDER
        SYSTEM_FAILURE
        REGULATORY_GAP
    }

    %% ── RELATIONSHIPS ────────────────────────────────────────────────

    ThreatFramework "1" --> "0..*" ThreatAnalysis : guides
    FunctionalNode "1" *-- "0..*" ThreatAnalysis : subject to
    ThreatAnalysis "1" --> "1..*" Threat : identifies

    Threat "1..*" --> "1..*" Vulnerability : exploits
    Vulnerability "1..*" --> "0..*" RiskAssessment : triggers
    Threat "1..*" --> "0..*" RiskAssessment : informs

    AssetContext "1..*" --> "0..*" RiskAssessment : scopes

    RiskAssessment "1" --> "0..*" MitigationRequirement : generates
    MitigationRequirement "1..*" --> "1" FunctionalNode : injected into
    MitigationRequirement "1..*" --> "1..*" Vulnerability : addresses

    %% ── FEEDBACK LOOP ────────────────────────────────────────────────
    %% New FunctionalNodes from MitigationRequirement re-enter
    %% Phase 3 Decomposition for ComplianceGate validation

    FunctionalNode "1" *-- "0..*" ComplianceGate : re-validates

    ThreatFramework ..> FrameworkType : uses
    Threat ..> ThreatSource : uses
    Vulnerability ..> SeverityLevel : uses
    RiskAssessment ..> RiskDecision : uses
    MitigationRequirement ..> MitigationStrategy : uses
    ThreatAnalysis ..> AnalysisStatus : uses
```
