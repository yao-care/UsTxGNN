---
layout: default
title: Diclofenac
parent: 僅模型預測 (L5)
nav_order: 602
evidence_level: L5
indication_count: 10
---

# Diclofenac
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Diclofenac: From Inflammatory Pain to Juvenile Idiopathic Arthritis

## One-Sentence Summary

Diclofenac is a non-selective COX-1/2 inhibitor (NSAID) established for pain and inflammatory conditions worldwide, though formal US license data was not captured in this Evidence Pack.
The TxGNN model identifies **Juvenile Idiopathic Arthritis (JIA)** as the highest-evidence repurposing candidate among the 10 predictions evaluated, supported by **2 clinical trials** and **18 publications** — including direct clinical trials of diclofenac in paediatric arthritis dating from the 1980s.
It is important to note that the model's top-ranked predictions (ranks 1–8) are all rare genetic diseases with no supporting evidence and are flagged as likely knowledge graph false positives; JIA (rank 9) is the only actionable candidate in this pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Inflammatory pain and musculoskeletal conditions (US license data not retrieved — see data gap note) |
| Predicted New Indication | Juvenile Idiopathic Arthritis |
| TxGNN Prediction Score | 99.25% |
| Evidence Level | L2 |
| US Market Status | Not captured (data gap — likely US-approved; see market section) |
| Number of NDAs | 0 retrieved (data gap) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Diclofenac is a non-selective cyclooxygenase inhibitor that blocks both COX-1 and COX-2, thereby suppressing prostaglandin biosynthesis. While the Evidence Pack did not retrieve formal MOA data from DrugBank (data gap DG002), the drug's mechanism is described consistently in the evidence literature: COX inhibition reduces prostaglandin E2 (PGE2) production, which is the common mediator of pain, fever, and inflammatory tissue responses.

Juvenile Idiopathic Arthritis is characterised by synovial inflammation in which COX-2 overexpression drives excess PGE2 generation, directly causing joint swelling, pain, and fever. Diclofenac's mechanism maps precisely onto this pathological axis. Crucially, this is not a speculative connection — the paediatric rheumatology literature from the 1980s already includes direct head-to-head clinical trials of diclofenac vs. naproxen and tolmetin in juvenile chronic arthritis, with comparable efficacy demonstrated across all three agents. Multiple subsequent reviews cite diclofenac as a standard first-line NSAID option for JIA.

By contrast, the model's top-8 predictions (ranks 1–8, scores 99.25–99.69%) cover rare genetic conditions such as hypotrichosis simplex, acromesomelic dysplasia, pseudoachondroplasia, and WHIM syndrome — diseases caused by structural gene mutations (LPAR6, CDMP1/GDF5, COMP, CXCR4, etc.) with no known connection to the COX/prostaglandin pathway. These predictions most likely arise from network proximity artefacts in the knowledge graph rather than genuine biological signal. JIA stands apart as the only prediction with both mechanistic coherence and clinical validation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00688545](https://clinicaltrials.gov/study/NCT00688545) | N/A (Observational Registry) | Terminated | 275 | SINCERE Registry: prospective multi-centre safety study comparing NSAIDs (including diclofenac) vs. celecoxib in JIA patients treated in clinical practice. Terminated early at 275 patients; provides real-world safety reference data but limited efficacy evidence due to observational design. |
| [NCT05871086](https://clinicaltrials.gov/study/NCT05871086) | Phase 2/3 | Unknown | 60 | Coenzyme Q10 supplementation in JIA (2023); NSAIDs cited as standard background therapy but are not the study intervention. Indirect relevance only — confirms current NSAID use in JIA practice. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [3052965](https://pubmed.ncbi.nlm.nih.gov/3052965/) | 1988 | RCT (crossover) | Clinical and Experimental Rheumatology | Single-blind crossover trial in 28 children with seronegative JCA comparing naproxen (10 mg/kg/day), diclofenac (2 mg/kg/day), and tolmetin (25 mg/kg/day) over 12 weeks; all three showed comparable clinical and laboratory efficacy with similar tolerability. |
| [6361986](https://pubmed.ncbi.nlm.nih.gov/6361986/) | 1983 | Clinical Trial | Scandinavian Journal of Rheumatology | Direct pharmacokinetic and clinical study of diclofenac sodium in juvenile rheumatoid arthritis; assessed plasma levels and renal elimination in children aged 2–7, providing foundational paediatric dosing data. |
| [2235663](https://pubmed.ncbi.nlm.nih.gov/2235663/) | 1990 | Clinical Study | Pediatria Medica e Chirurgica | Open non-comparative study of diclofenac sodium in 26 patients (aged 2–16) with polyarticular juvenile chronic arthritis; confirmed anti-inflammatory and analgesic effects consistent with adult data. |
| [10756785](https://pubmed.ncbi.nlm.nih.gov/10756785/) | 1997 | Comparative Study | Revista Medico-Chirurgicala | Eight-year comparative study of diclofenac vs. ibuprofen vs. aspirin in 100 children with JCA; evaluated clinical and laboratory outcomes at multiple time points up to 3 years of follow-up. |
| [8422565](https://pubmed.ncbi.nlm.nih.gov/8422565/) | 1993 | Review | British Journal of Rheumatology | Comprehensive review of NSAID use in paediatric rheumatic diseases; explicitly states diclofenac, ibuprofen, tolmetin, and naproxen are equal in efficacy and tolerability for JCA joint symptom control; aspirin and indomethacin are more toxic without added benefit. |
| [11735667](https://pubmed.ncbi.nlm.nih.gov/11735667/) | 2001 | Review (Risk-Benefit) | Paediatric Drugs | Risk-benefit analysis of NSAIDs in children including JIA and Kawasaki disease; covers COX inhibition mechanism, paediatric pharmacokinetics, and safety profile including GI, renal, and bleeding risks. |
| [1884567](https://pubmed.ncbi.nlm.nih.gov/1884567/) | 1991 | PK Study | Clinical Pharmacokinetics | Pharmacokinetic review of drugs used in juvenile arthritis, including NSAIDs; provides dosing rationale and metabolic considerations relevant to diclofenac use in the paediatric JIA population. |
| [17474954](https://pubmed.ncbi.nlm.nih.gov/17474954/) | 2007 | Survey | Paediatric Anaesthesia | UK/Ireland survey noting that diclofenac is licensed for children over 1 year for juvenile rheumatoid arthritis treatment; highlights paediatric NSAID licensing landscape. |
| [723822](https://pubmed.ncbi.nlm.nih.gov/723822/) | 1978 | Clinical Study | Minerva Pediatrica | One of the earliest clinical studies of sodium diclofenac in infantile rheumatoid arthritis, establishing initial paediatric safety and efficacy signal. |
| [6761640](https://pubmed.ncbi.nlm.nih.gov/6761640/) | 1982 | Clinical Study | Pediatriia | Soviet clinical study of Voltaren (diclofenac) in children with rheumatoid arthritis; corroborates efficacy findings from Western paediatric rheumatology literature. |

---

## US Market Information

No US market authorizations were retrieved for Diclofenac in this Evidence Pack (market status recorded as "未上市," 0 NDAs). This is very likely a **data retrieval gap** rather than a true absence: diclofenac is approved in the United States under multiple brand names (e.g., Voltaren Gel, Zipsor, Cambia, Pennsaid) across both oral and topical formulations.

Manual verification against the FDA Orange Book is recommended before relying on the market status recorded here. The data gap DG001 (TFDA package insert) and the US market retrieval failure should both be resolved before proceeding to formal safety evaluation.

---

## Safety Considerations

Please refer to the package insert for safety information.

> All safety fields in this Evidence Pack are marked as data gaps (DG001). Standard NSAID class warnings — including GI bleeding risk, renal impairment, cardiovascular risk, and contraindication in third-trimester pregnancy — apply and must be retrieved from the official labelling before any clinical decision is made.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The JIA repurposing direction is mechanistically coherent (COX-mediated synovial inflammation) and is clinically validated by direct paediatric clinical trials spanning four decades — including at least one randomised crossover study. In practice, this may represent the TxGNN model correctly recovering an established (though perhaps unlabelled) indication rather than a genuinely novel repurposing discovery, which itself validates the model's predictive signal for this drug class.

**To proceed, the following is needed:**

- **Resolve US market status**: Retrieve NDAs from the FDA Orange Book manually; the "未上市" in this pack is almost certainly a data gap for a globally established drug
- **Retrieve DrugBank MOA data (DG002)**: Formally confirm COX-1/2 inhibition profile and any additional pharmacological targets for the evidence file
- **Retrieve package insert warnings and contraindications (DG001)**: Required to complete the S1 safety evaluation; standard NSAID risks (GI, renal, cardiovascular) are expected to apply
- **Clarify indication status**: Determine whether JIA is already a formally approved indication for diclofenac in the US (in which case this is indication-label confirmation rather than repurposing, and regulatory strategy differs accordingly)
- **Review ranks 1–8 false positive pattern**: All 8 top-scored predictions are rare genetic diseases with no COX-pathway connection; this warrants a calibration review of the TxGNN model's knowledge graph for this drug to assess systematic bias in scoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

