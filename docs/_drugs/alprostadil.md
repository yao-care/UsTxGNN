---
layout: default
title: Alprostadil
parent: Moderate Evidence (L3-L4)
nav_order: 269
evidence_level: L3
indication_count: 10
---

# Alprostadil
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Alprostadil: From Approved Use (Not Specified in the Data) to Aortic Malformation

## One-Sentence Summary

Alprostadil (prostaglandin E1) is a marketed injectable in the US, but the input data does not list its approved indication text.
The TxGNN model predicts it may be useful for **aortic malformation**, mainly as a neonatal bridge that keeps the ductus arteriosus open until surgery.
Support is limited to **2 registered clinical trials** (neither is an efficacy trial) and **20 publications** (reviews, case series and case reports, no RCTs).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the provided data (all license records have empty indication text) |
| Predicted New Indication | Aortic malformation |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 12 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the input. Alprostadil is the synthetic form of prostaglandin E1 (PGE1). PGE1 relaxes the smooth muscle of the ductus arteriosus and keeps it open.

Some aortic malformations, such as interrupted aortic arch, critical aortic stenosis and aortic atresia, make the newborn's systemic circulation depend on blood flowing through the ductus. Keeping the ductus open maintains systemic perfusion until surgical repair. The literature describes PGE1 as having transformed the management of interrupted aortic arch since the late 1970s.

The mechanism is direct and biologically plausible. However, the evidence comes from a Phase 1 trial and retrospective or narrative literature, so the evidence level is capped at L3. The on-label status of this use should be verified against the US labeling, because the approved indication text is missing from the input.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04054115](https://clinicaltrials.gov/study/NCT04054115) | Phase 1 | Terminated | 10 | Acute effects of alprostadil on cerebral and pulmonary blood flow after bidirectional cavopulmonary connection (single-ventricle palliation). Terminated early, so it gives a physiologic and safety signal, not efficacy evidence. The population is adjacent to aortic malformation. |
| [NCT02042092](https://clinicaltrials.gov/study/NCT02042092) | N/A | Completed | 39 | Cross-sectional comparison of Doppler ultrasound and MR angiography in large-vessel vasculitis. Diagnostic imaging only. It does not test alprostadil and is of low relevance. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26686446](https://pubmed.ncbi.nlm.nih.gov/26686446/) | 2015 | Review | Semin Thorac Cardiovasc Surg | PGE1 revolutionized interrupted aortic arch management. Resuscitation is followed by one-stage neonatal repair. |
| [25647388](https://pubmed.ncbi.nlm.nih.gov/25647388/) | 2014 | Review | Cardiol Young | Preoperative management of neonatal critical aortic stenosis. It remains a high-morbidity, high-mortality condition. |
| [30347623](https://pubmed.ncbi.nlm.nih.gov/30347623/) | 2019 | Review | J Neonatal Perinat Med | Enteral feeding strategies and necrotising enterocolitis risk in infants on PGE1 infusion for duct-dependent heart disease. |
| [6763200](https://pubmed.ncbi.nlm.nih.gov/6763200/) | 1982 | Case series | Pharmacotherapy | Alprostadil dilates the ductus and improves flow in newborns with ductus-dependent congenital defects. |
| [7201134](https://pubmed.ncbi.nlm.nih.gov/7201134/) | 1982 | Case series | Pediatr Cardiol | PGE1 in 7 infants with hypoplastic left ventricle and aortic atresia. Six showed transient improvement, but most non-operated patients died. |
| [6537955](https://pubmed.ncbi.nlm.nih.gov/6537955/) | 1984 | Case series | J Am Coll Cardiol | Long-term PGE1 in 17 neonates with ductus-dependent lesions, including aortic coarctation. |
| [31010402](https://pubmed.ncbi.nlm.nih.gov/31010402/) | 2020 | Case report | World J Pediatr Congenit Heart Surg | PGE1 bridged a premature newborn with severe coarctation and closed ductus to surgical repair. The report suggests a role even without a patent ductus. |
| [32184038](https://pubmed.ncbi.nlm.nih.gov/32184038/) | 2020 | Cohort | Asian J Surg | Outcomes of a staged-repair policy for infants with interrupted aortic arch. |
| [1926911](https://pubmed.ncbi.nlm.nih.gov/1926911/) | 1991 | Not classified | DICP | Starting PGE1 before neonatal transport is recommended when a ductus-dependent defect is suspected. |
| [25263728](https://pubmed.ncbi.nlm.nih.gov/25263728/) | 2014 | Case report | J Perinatol | Transient hypertrophic pyloric stenosis after prolonged PGE1 infusion (safety signal). |

## US Market Information

The input lists 12 licenses in total. Four distinct main authorizations are shown below (NDA020379 appears twice in the input and is merged here).

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020379 | Caverject | Lyophilized powder for injection solution | Not listed in the input |
| NDA021212 | Caverject Impulse | Lyophilized powder for injection solution | Not listed in the input |
| NDA018484 | PROSTIN | Injection solution | Not listed in the input |
| NDA020649 | Edex | Lyophilized powder for injection solution | Not listed in the input |

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the DDI query.
- **Literature-reported adverse effects**: Prolonged PGE1 infusion in neonates has been linked to gastric outlet obstruction (antral foveolar hyperplasia, transient hypertrophic pyloric stenosis). Other commonly reported effects are apnea, fever, hypotension, rash and flushing. Necrotising enterocolitis risk with enteral feeding has also been studied.

Structured warnings and contraindications were not retrieved. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is direct and consistent across decades of case series and reviews on ductus-dependent aortic lesions. However, there are no completed efficacy trials, and the only registered alprostadil trial is a terminated Phase 1 study. Use should therefore be limited to the guardrails below.

- Neonatal intensive care setting only
- Monitoring for apnea, hypotension and fever
- Lowest effective dose for the shortest duration

**To proceed, the following is needed:**
- The FDA package insert (warnings, contraindications, approved indications) to confirm on-label status. This gap currently blocks safety screening.
- Mechanism-of-action data from DrugBank
- A structured review of the retrospective literature, including outcomes and adverse-event rates for PGE1 in interrupted aortic arch, critical aortic stenosis and aortic atresia
- Verification of dosage-form and route compatibility. Available products are injectables, but suitability for neonatal infusion is not confirmed in the data.

Other predicted indications are weaker. Congenital tricuspid stenosis and heart septal defect are research questions at best, since PGE1 acts through ductus-dependent physiology rather than the named lesion. Endemic goiter is likely a false positive.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

