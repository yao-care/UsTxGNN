---
layout: default
title: Papaverine
parent: 僅模型預測 (L5)
nav_order: 1014
evidence_level: L5
indication_count: 10
---

# Papaverine
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

# Papaverine: From Vasospasm Treatment to Ischemic Disease

## One-Sentence Summary

> Papaverine has long been used clinically as an intra-arterial/intracavernosal vasodilator to prevent or treat vascular spasm (e.g., during CABG graft harvesting, mesenteric ischemia, and coronary flow reserve testing), though it currently holds no formal marketing authorization in this jurisdiction.
> The TxGNN model predicts it may be effective for **Ischemic Disease**,
> with **4 clinical trials** and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication text found in this jurisdiction's licensing records |
| Predicted New Indication | Ischemic Disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L3 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (data gap). Based on the clinical evidence collected in this evidence pack, papaverine is well documented as a non-selective phosphodiesterase (PDE3/PDE4) inhibitor that relaxes vascular smooth muscle by raising intracellular cAMP/cGMP levels. Clinically, it has been used for decades as an intra-arterial and intraluminal vasodilator — for example, to prevent graft spasm during internal thoracic/radial artery harvesting in CABG, to treat non-occlusive mesenteric ischemia, and to measure coronary flow reserve during catheterization.

This existing vasodilatory / anti-vasospastic role is mechanistically consistent with the pathophysiology of ischemic disease, where impaired tissue perfusion due to vasospasm or reduced vascular flow reserve is a central feature. In this sense, the TxGNN prediction largely formalizes an already-established clinical practice pattern rather than proposing an entirely novel hypothesis — papaverine is already used as an adjunct in ischemia-related procedures, but rigorous therapeutic-endpoint trials specifically targeting "ischemic disease" as a formal indication remain limited.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06014242](https://clinicaltrials.gov/study/NCT06014242) | NA | Withdrawn | 0 | Peripheral microvascular resistance as a predictor of limb salvage in critical limb ischemia; withdrawn with no data. |
| [NCT06795035](https://clinicaltrials.gov/study/NCT06795035) | N/A | Recruiting | 70 | Coronary microvascular dysfunction after STEMI assessed via continuous saline thermodilution; papaverine relevant to CFR/microvascular resistance testing methodology. |
| [NCT05562908](https://clinicaltrials.gov/study/NCT05562908) | NA | Completed | 165 | Skeletonised vs. pedicled internal thoracic artery harvesting for CABG; papaverine used as standard intraoperative anti-spasm treatment. |
| [NCT06125392](https://clinicaltrials.gov/study/NCT06125392) | N/A | Recruiting | 1000 | Multicenter registry on chronic angina without obstructive coronary stenosis, seeking a new acetylcholine-spasm definition. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3661361](https://pubmed.ncbi.nlm.nih.gov/3661361/) | 1987 | Cohort | American Heart Journal | Intracoronary papaverine superior to radiographic contrast for measuring coronary flow reserve in ischemic heart disease. |
| [12964071](https://pubmed.ncbi.nlm.nih.gov/12964071/) | 2003 | Review | RoFo | Review of non-occlusive mesenteric ischemia; discusses vasodilator therapy including papaverine infusion. |
| [7590571](https://pubmed.ncbi.nlm.nih.gov/7590571/) | 1995 | Review | Hepato-Gastroenterology | Non-occlusive mesenteric ischemia pathophysiology and vasodilator treatment approaches. |
| [32713799](https://pubmed.ncbi.nlm.nih.gov/32713799/) | 2020 | Preclinical/Mechanistic | J Pharmacol Sci | Papaverine shows anti-inflammatory/immunomodulatory effects and reduces infarct volume in a mouse cerebral ischemia model. |
| [28832798](https://pubmed.ncbi.nlm.nih.gov/28832798/) | 2017 | Preclinical | Braz J Cardiovasc Surg | Papaverine + ascorbic acid reduced liver injury from ischemia-reperfusion after aortic cross-clamping in rats. |
| [16368347](https://pubmed.ncbi.nlm.nih.gov/16368347/) | 2006 | Not classified | Ann Thorac Surg | Compared papaverine vs. glyceryl-trinitrate/verapamil as topical/intraluminal vasodilators for internal thoracic artery spasm. |
| [9972912](https://pubmed.ncbi.nlm.nih.gov/9972912/) | 1998 | Not classified | J Cardiovasc Surg | Intrathecal papaverine plus cooling extended safe aortic cross-clamping time via spinal cord protection in a porcine model. |
| [831413](https://pubmed.ncbi.nlm.nih.gov/831413/) | 1977 | Not classified | American Heart Journal | Compared papaverine and adenosine effects on myocardial blood flow during coronary reperfusion. |
| [8293164](https://pubmed.ncbi.nlm.nih.gov/8293164/) | 1993 | Not classified | Current Opinion in Neurology | Reviews superselective intra-arterial papaverine infusion for cerebral vasospasm after aneurysm rupture. |
| [9674923](https://pubmed.ncbi.nlm.nih.gov/9674923/) | 1998 | Not classified | Microsurgery | In vitro/in vivo comparison of lidocaine and papaverine vasodilation for flap ischemia prevention. |

---

## US Market Information

Currently not marketed — no authorization/license records were found for this drug in this jurisdiction (0 NDAs on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Papaverine's vasodilatory/anti-vasospastic mechanism is well documented and already used clinically as an adjunct in ischemia-related procedures (graft spasm prevention, mesenteric ischemia, coronary flow reserve testing), giving the TxGNN prediction reasonable mechanistic and observational support (L3). However, no dedicated Phase 2/3 RCT establishes papaverine as a primary therapy for "ischemic disease" as a standalone indication, and the drug currently has no marketing authorization in this jurisdiction.

**To proceed, the following is needed:**
- **Blocking gap (DG001)**: TFDA/local regulatory label warnings and contraindications must be obtained (e.g., via label PDF retrieval) before any S1 safety review can proceed.
- **High-priority gap (DG002)**: Formal mechanism-of-action documentation (e.g., from DrugBank API) to support mechanistic-link analysis.
- Confirmation of route compatibility (currently marked "pending") between required administration route for ischemic disease treatment and available formulations.
- A dedicated interventional trial with ischemic disease as the primary efficacy endpoint, rather than papaverine's current role as a diagnostic/procedural adjunct.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

