---
layout: default
title: Chloroquine
parent: Model Prediction Only (L5)
nav_order: 521
evidence_level: L5
indication_count: 4
monitor_inn: "CHLOROQUINE"
predicted_indications: ["rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "rheumatoid nodulosis", "juvenile chronic polyarthritis", "juvenile idiopathic arthritis"]
last_modified_at: 2026-10-14
description: "Chloroquine: predicted new indication Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis (evidence level L5). Approved use: Rheumatoid arthritis, systemic lupus erythematosus, mal…"
---

# Chloroquine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Chloroquine: From Rheumatoid Arthritis and Malaria to Rheumatoid Factor-Positive Polyarticular Juvenile Idiopathic Arthritis

## One-Sentence Summary

Chloroquine is an antimalarial that is also used for rheumatoid arthritis and lupus.
The TxGNN model predicts it may be effective for **rheumatoid factor-positive polyarticular juvenile idiopathic arthritis**,
but currently **0 clinical trials** and only **1 publication** (a leflunomide study that does not assess chloroquine) support this direction, so the prediction rests mainly on the model score.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, systemic lupus erythematosus, malaria (P. vivax, P. falciparum, P. ovale, P. malariae), discoid and chronic cutaneous lupus erythematosus |
| Predicted New Indication | Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid authorizations) |
| Number of NDAs | 6 (all cancelled; the records are ANDA or unnumbered entries) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, chloroquine is an antimalarial whose efficacy in rheumatoid arthritis and lupus is established. Its immunomodulatory effects (reduced lysosomal acidification, altered antigen processing, and dampened Toll-like receptor signaling) could plausibly apply to autoimmune arthritis in children.

RF-positive polyarticular JIA is the pediatric disease most similar to adult rheumatoid arthritis, which is an original indication of chloroquine. The high TxGNN score likely reflects this closeness to the approved RA indication.

However, no chloroquine-specific clinical evidence was found for this exact subtype. The mechanistic link remains a hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24334641](https://pubmed.ncbi.nlm.nih.gov/24334641/) | 2014 | Cohort | The Journal of Rheumatology | Long-term real-life experience with leflunomide in JIA. It does not evaluate chloroquine, so it offers only indirect context on JIA treatment. |

For the broader JIA category, historical papers (1971-1991) describe chloroquine dosing and use in juvenile arthritis, and one cohort (PMID 18021335) examined methotrexate pharmacokinetics with and without chloroquine. These are indirect and not controlled efficacy data.

## US Market Information

All six records are cancelled; none is currently valid. Approved indication text is not available for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA040516 | Chloroquine Phosphate (Amneal) | Tablet | Not available (cancelled) |
| ANDA214756 | Chloroquine Phosphate (Suven) | Tablet, coated | Not available (cancelled) |
| ANDA091621 | Chloroquine Phosphate (Rising) | Tablet | Not available (cancelled) |
| ANDA090612 | Chloroquine Phosphate (Rising) | Tablet | Not available (cancelled) |
| ANDA080880 | Chloroquine Phosphate (Amneal) | Tablet | Not available (cancelled) |

A sixth record, Chloroquinum Phos. (Hahnemann Laboratories, pellet), has no authorization number.

## Safety Considerations

Package-insert warnings and contraindications were not available. The following comes from knowledge-graph contraindication links and drug interaction screening.

- **Contraindication links (knowledge graph, not label text)**: epilepsy; porphyria; liver and gallbladder disease; eye and retinal disease, vision disorders, scotoma; hearing disorders; psoriasis; neutropenia, agranulocytosis, leukopenia; anemia; G6PD deficiency; glycogen storage disease, cystinuria, galactosemia; substance abuse/dependence.
- **Drug Interactions**: 100 interactions were found; the first 20 reviewed include several rated **Major**: agalsidase beta, bupropion, cisapride, clarithromycin, dolasetron, and granisetron. Moderate interactions include antacids (aluminum hydroxide, calcium carbonate), H2 blockers (famotidine, cimetidine), sulfonylureas and insulin (hypoglycemia risk), metronidazole, loperamide, and aprepitant. Several Major pairs are QT-prolonging agents.
- **Pediatric concerns from the literature**: a case report documents third-degree atrioventricular block on chloroquine (PMID 9523387), and another reports chloroquine-induced vitiligo in juvenile-onset RA. Retinal toxicity would also need careful attention in children.

Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score and the similarity to adult RA. There are no registered trials, and the only retrieved paper for this subtype concerns leflunomide, not chloroquine. Chloroquine is also cancelled-only on the US market, and pediatric retinal and cardiac safety concerns exist. Hydroxychloroquine would likely be a more practical comparator.

**To proceed, the following is needed:**
- Mechanism of action data and FDA package insert warnings and contraindications (both currently missing)
- Chloroquine-specific clinical data in JIA, ideally from a modern controlled study or a comparison with hydroxychloroquine
- A pediatric safety plan covering retinal screening, cardiac (QT/conduction) monitoring, and interaction management
- Clarification of drug availability, given that all US authorizations are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

