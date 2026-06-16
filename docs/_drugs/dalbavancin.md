---
layout: default
title: Dalbavancin
parent: 僅模型預測 (L5)
nav_order: 565
evidence_level: L5
indication_count: 10
---

# Dalbavancin
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

# Dalbavancin: From Acute Bacterial Skin Infections to Post-Bacterial Disorder

## One-Sentence Summary

Dalbavancin (Dalvance) is a long-acting lipoglycopeptide antibiotic FDA-approved in the United States for acute bacterial skin and skin structure infections (ABSSSI) caused by susceptible Gram-positive organisms, including MRSA.
The TxGNN model predicts it may be effective for **post-bacterial disorder** — a category encompassing complicated Gram-positive infections such as bacteremia, infective endocarditis, and osteoarticular infections —
with **13 clinical trials** (including two landmark Phase 3 pivotal studies) currently supporting this direction, placing the evidence at **L1**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute Bacterial Skin and Skin Structure Infections (ABSSSI) caused by Gram-positive organisms |
| Predicted New Indication | Post-Bacterial Disorder |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L1 |
| Taiwan Market Status | Not marketed (no TFDA licenses) |
| Number of TFDA Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Dalbavancin is a second-generation lipoglycopeptide antibiotic that inhibits bacterial cell wall biosynthesis by binding to the D-Ala-D-Ala terminus of peptidoglycan precursors, thereby blocking transpeptidation and transglycosylation. Its most distinctive pharmacokinetic property is an exceptionally long half-life of approximately 346 hours, which allows once-weekly or even single-dose IV regimens — a unique advantage over conventional antibiotics like vancomycin that require daily or twice-daily infusions.

The mechanistic connection between ABSSSI and post-bacterial disorder is direct rather than inferential: both involve the same Gram-positive pathogen spectrum (MRSA, MSSA, *Streptococcus* spp.), and dalbavancin's antibacterial activity is identical regardless of whether the infection site is the skin or deeper structures such as bone, bloodstream, or heart valves. The DISCOVER 1 and DISCOVER 2 pivotal trials (n = 739 and 573 respectively) established the foundation, while the subsequent DOTS trial (Phase 2b, n = 200) directly expanded the evidence base to complicated *S. aureus* bacteremia and right-sided infective endocarditis — key subcategories squarely within post-bacterial disorder.

The single-dose convenience of dalbavancin is particularly compelling for the outpatient parenteral antibiotic therapy (OPAT) model: patients traditionally requiring 4–6 weeks of daily IV antibiotics for osteomyelitis or bacteremia can potentially be discharged earlier, reducing hospital-acquired complications and costs. This represents a genuine clinical advantage rather than a marginal improvement, which the ongoing Phase 3 trial NCT05117398 is positioned to further validate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01431339](https://clinicaltrials.gov/study/NCT01431339) | Phase 3 | Completed | 739 | DISCOVER 1: double-blind RCT comparing dalbavancin vs vancomycin/linezolid for ABSSSI; co-pivotal trial establishing US FDA approval |
| [NCT01339091](https://clinicaltrials.gov/study/NCT01339091) | Phase 3 | Completed | 573 | DISCOVER 2: confirmatory pivotal RCT vs vancomycin/linezolid for suspected or proven Gram-positive ABSSSI; together with DISCOVER 1, forms the L1 evidence base |
| [NCT04775953](https://clinicaltrials.gov/study/NCT04775953) | Phase 2b | Completed | 200 | DOTS trial: dalbavancin vs standard-of-care for completion of treatment in complicated *S. aureus* bacteremia and right-sided native valve infective endocarditis; supports bacteremia extension |
| [NCT05117398](https://clinicaltrials.gov/study/NCT05117398) | Phase 3 | Recruiting | 406 | Single-dose dalbavancin 1500 mg vs 14-day standard antibiotic therapy for catheter-related *S. aureus* bloodstream infections; non-inferiority design, completion Sept 2026 |
| [NCT02127970](https://clinicaltrials.gov/study/NCT02127970) | Phase 3b | Completed | 698 | Single-dose (1500 mg) vs two-dose regimen for ABSSSI; directly supported regulatory approval of simplified single-dose administration |
| [NCT02814916](https://clinicaltrials.gov/study/NCT02814916) | Phase 3 | Completed | 199 | Pediatric ABSSSI safety and descriptive efficacy study (birth to 17 years) for known/suspected Gram-positive infections including MRSA strains |
| [NCT03233438](https://clinicaltrials.gov/study/NCT03233438) | Phase 4 | Completed | 91 | Real-world critical pathway evaluation: guideline-based patient identification + dalbavancin vs usual care for ABSSSI; assessed healthcare utilization outcomes |
| [NCT06810583](https://clinicaltrials.gov/study/NCT06810583) | Phase 1 | Recruiting | 29 | Dalbavancin-based prophylaxis in pediatric AML/relapsed ALL patients receiving myelosuppressive chemotherapy; characterizes PK and bacteremia prevention rate |
| [NCT04847921](https://clinicaltrials.gov/study/NCT04847921) | Phase 2/3 | Terminated | 11 | 2-dose dalbavancin for severe Gram-positive infections in people who use drugs (PWUD); terminated early due to enrollment difficulties, limited interpretable data |
| [NCT06688084](https://clinicaltrials.gov/study/NCT06688084) | N/A | Active, not recruiting | 230 | Observational study of *S. pettenkoferi* pathogenicity in diabetic foot wounds and osteitis; background epidemiological context for Gram-positive post-bacterial disorder |

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Dalbavancin is currently **not marketed in Taiwan**. No TFDA authorization records were found.

> **For reference:** Dalbavancin is approved by the US FDA under the brand name **Dalvance** (AbbVie, originally Durata Therapeutics), first approved in May 2014 for ABSSSI in adults, with subsequent label updates. This US approval and the underlying clinical trial data form the primary evidence base for this report.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Detailed warning and contraindication data from TFDA prescribing information was not available at the time of this analysis. US Dalvance prescribing information should be consulted for full safety details, including hypersensitivity to glycopeptides, *C. difficile*-associated diarrhea risk, and hepatic impairment guidance.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The DISCOVER 1/2 pivotal trials (combined n = 1,312) provide L1 evidence for dalbavancin against Gram-positive infections, and the DOTS Phase 2b trial directly validates its use in *S. aureus* bacteremia — a core component of "post-bacterial disorder." The drug's unique pharmacokinetics (single-dose, week-long coverage) address a genuine unmet clinical need in OPAT settings, and an ongoing Phase 3 trial (NCT05117398, n = 406, expected completion Sept 2026) will further strengthen the evidence base for bloodstream infections.

**To proceed, the following is needed:**

- Obtain full MOA and safety profile from DrugBank API (currently a data gap flagged as High severity)
- Review US Dalvance prescribing information for contraindications, warnings, and drug interactions before any TFDA submission planning
- Define the specific target sub-indication within post-bacterial disorder (e.g., *S. aureus* bacteremia completion therapy, osteomyelitis OPAT, or infective endocarditis step-down)
- Monitor NCT05117398 results (expected Sept 2026) — if non-inferiority is demonstrated, this provides the strongest single-agent evidence for bacteremia expansion
- Commission a cost-effectiveness analysis for the OPAT model versus standard daily IV therapy in Taiwan's healthcare system
- Note: Three other TxGNN-predicted indications (postinfectious vasculitis, Chagas cardiomyopathy, infectious mononucleosis) have been assessed and are scientifically implausible given dalbavancin's purely antibacterial mechanism — no further investigation is warranted for these
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

