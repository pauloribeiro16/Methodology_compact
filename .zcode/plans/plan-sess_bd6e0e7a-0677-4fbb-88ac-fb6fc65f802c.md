# Conversão dos pilots ao template Bike4All (RUP-style)

**Objectivo:** reescrever as secções piloto (PKG-8 no Doc21 do Case_02, PKG-C no Doc22 do Case_03) do formato compacto actual para o template de 9+1 secções do documento de referência `03_REFERENCE_MATERIAL/P3_E2_Requirement_Analysis_Bike4All_Maintenance_platform_v1r2.md`, com os ajustes AEGIS.

## Estrutura por UC (template + ajustes)
```
#### Use-Case: {U.C.8.1.1} Scan Travel Document (MRZ + NFC chip)
##### 1 Brief Description        (voz de produto; inclui o trigger)
##### 2 Actor Brief Descriptions (###### 2.n por actor, incl. SYS-04 kiosk)
##### 3 Preconditions
##### 4 Basic Flow of Events     (Main Success Scenario)
    + sequenceDiagram Mermaid (4-8 linhas, convenções 00_METHODOLOGY/diagrams)
##### 5 Alternative Flows        (###### 5.n <Alternate flow: Name>)
##### 6 Subflows                 (NOVO: fragmentos reutilizáveis, ex. purga de template)
##### 7 Key Scenarios            (sucesso + falha principal)
##### 8 Post-conditions
##### 9 Special Requirements (FURPS+)  (só factos atestados; N/A onde não há)
##### 10 Security & Compliance Annex (AEGIS)  ← a nossa camada: Provenance / Constrained by / Rules / Threats (MUC) / NIST anchors
```

## Regras de conversão
- **Zero mudança de conteúdo**: todos os IDs, regras CR-/BPR-, MUCs, âncoras NIST e provenance atestada preservados verbatim; subflows/scenarios/FURPS derivados apenas dos factos existentes (N/A onde não há facto, prática do próprio reference).
- **Nomenclatura intacta**: U.C.8.x.y (C2), UC-63..68 flat (C3), compliance verbatim, MUC cards intocados.
- Diagramas Mermaid: 1 por UC (13 no total), sintaxe simples e correcta.
- Notas de intro actualizadas (menção ao template Bike4All + ajustes AEGIS).

## Ficheiros tocados (só estes)
- `02_CASES/Case_02_SecureBorder_Solutions/03_PHASE3_DECOMPOSITION/Doc21_Use_Cases_Catalog.md` (§6.1)
- `02_CASES/Case_03_OmniBank_Financial/03_PHASE3_DECOMPOSITION/Doc22_Use_Cases_Catalog.md` (§6B.1)

## Gates
check_unmapped C2+C3 PASS · verify_rich C2 "2 FAIL/6 PASS" e C3 "3 FAIL/5 PASS" (baselines, sem novos FAILs) · sanidade: 7 + 6 blocos UC, 13 mermaid, 10 secções/UC · depois commit e seguimos para a tua revisão (Fase 3) e depois massificação + risco OWASP.

O plano de execução detalhado (subflows/FURPS por UC) já foi desenhado pelo subagente e está pronto a correr.