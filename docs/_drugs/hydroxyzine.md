---
layout: default
title: Hydroxyzine
parent: Moderate Evidence (L3-L4)
nav_order: 782
evidence_level: L4
indication_count: 5
---

# Hydroxyzine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

# Hydroxyzine: From First-Generation Antihistamine to Allergic Urticaria

## One-Sentence Summary

Hydroxyzine is a first-generation H1-receptor antihistamine that is marketed in the US in tablet, capsule and solution forms.
The TxGNN model predicts it may be effective for **allergic urticaria**, but the evidence is only class-level: **1 clinical trial** (which does not study hydroxyzine) and **20 publications** (mostly reviews of other antihistamines).
Hydroxyzine is already widely used for itch and urticaria, so this may be an existing use rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for hydroxyzine is not available in the source data. Based on known pharmacology, hydroxyzine is an H1-receptor inverse agonist. In urticaria, histamine released from mast cells causes the wheals, flare and itch. Blocking H1 receptors targets that pathway directly, which makes the prediction biologically plausible and fits the very high TxGNN score.

Several points limit how much weight the prediction deserves:

- The retrieved evidence is about other antihistamines (cetirizine, levocetirizine, bilastine, desloratadine), not hydroxyzine itself.
- Cetirizine is a metabolite of hydroxyzine (PMID 1981354), so cetirizine data gives only indirect support.
- The source data lists no original indication for hydroxyzine, and the approved-indication text for the US products is empty. Whether allergic urticaria is already on the label needs to be checked before treating it as a new indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | Completed | 36 | Small feasibility pilot comparing IV cetirizine 10 mg with IV diphenhydramine 50 mg in acute urticaria. It does not appear to study hydroxyzine (relevance grade C), so it gives only indirect class-level support. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31582993](https://pubmed.ncbi.nlm.nih.gov/31582993/) | 2019 | Position statement | Allergy Asthma Clin Immunol | CSACI states that newer-generation H1-antihistamines should be first-line for allergic rhinitis and urticaria. First-generation agents such as hydroxyzine cause sedation, cognitive impairment, dry mouth, dizziness and orthostatic hypotension, and have been linked to accidents, overdoses and sudden cardiac death. |
| [28913986](https://pubmed.ncbi.nlm.nih.gov/28913986/) | 2017 | Review | Allergy Asthma Immunol Res | Chronic spontaneous urticaria treatment starts with antihistamines, usually at doses above those used for rhinitis. Hydroxyzine and diphenhydramine were used this way in the past. Omalizumab is the option if high-dose antihistamines fail. |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Review | Drugs | Cetirizine, a carboxylated metabolite of hydroxyzine, is a potent peripheral H1 antagonist that lacks the CNS depressant effects of standard antihistamines. Reviews its clinical potential in chronic urticaria. |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Reviews the efficacy and safety of first- and newer-generation antihistamines in allergic rhinitis and chronic idiopathic urticaria. |
| [18336052](https://pubmed.ncbi.nlm.nih.gov/18336052/) | 2008 | Review | Clin Pharmacokinet | Comparative pharmacokinetic and pharmacodynamic review of desloratadine, fexofenadine and levocetirizine. Second-generation agents were developed to treat rhinitis and chronic idiopathic urticaria with fewer adverse effects. |
| [22994340](https://pubmed.ncbi.nlm.nih.gov/22994340/) | 2012 | Review | Clin Exp Allergy | Discusses how to choose the best H1-antihistamine in urticaria and the difficulty of comparing drugs without head-to-head studies. |
| [22686617](https://pubmed.ncbi.nlm.nih.gov/22686617/) | 2012 | Review | Drugs | Bilastine, a second-generation antihistamine, is used for allergic rhinoconjunctivitis and urticaria. |
| [18201439](https://pubmed.ncbi.nlm.nih.gov/18201439/) | 2007 | Review | Allergy Asthma Proc | Reviews levocetirizine's pharmacology, safety and effectiveness in allergic rhinitis and chronic idiopathic urticaria. |
| [19808127](https://pubmed.ncbi.nlm.nih.gov/19808127/) | 2009 | Review | Clin Ther | Levocetirizine is approved for allergic rhinitis and chronic idiopathic urticaria in adults and children aged 6 and over. |
| [12113226](https://pubmed.ncbi.nlm.nih.gov/12113226/) | 2002 | Review | Clin Allergy Immunol | Reviews H1-antagonist use in children, with strong evidence for allergic rhinoconjunctivitis. |

---

## US Market Information

The source data lists 20 US authorizations. The five main ones are below. Approved-indication text is empty for all of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA217652 | Hydroxyzine Hydrochloride | Tablet, film coated | Rising Pharma Holdings, Inc. |
| ANDA087479 | Hydroxyzine Pamoate | Capsule | Bryant Ranch Prepack |
| ANDA088487 | Hydroxyzine Pamoate | Capsule | Teva Pharmaceuticals USA, Inc. |
| ANDA204279 | Hydroxyzine Hydrochloride | Tablet, film coated | Bryant Ranch Prepack |
| ANDA087871 | Hydroxyzine Hydrochloride | Tablet, film coated | Bryant Ranch Prepack |

Other forms on the US market include plain tablets and solution.

---

## Safety Considerations

Please refer to the package insert for warnings, contraindications and drug interactions. The source data has no label-derived safety information, and the drug-interaction query returned no results.

The literature does raise one guardrail. The CSACI 2019 position statement (PMID 31582993) cautions that first-generation antihistamines such as hydroxyzine cause:

- Sedation and impaired cognition.
- Anticholinergic effects such as dry mouth.
- Orthostatic hypotension.
- Reports of sudden cardiac death.

The related QT-prolongation concern would need review against the label.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and the TxGNN score is very high. However, the supplied trial and literature evidence is class-level and not specific to hydroxyzine. The safety data needed for screening is missing. Current guidance favors second-generation antihistamines first-line, and allergic urticaria may already be an established hydroxyzine use.

**To proceed, the following is needed:**
- The US package insert (indications, warnings, contraindications), to confirm whether urticaria is already labeled and to complete safety screening.
- Detailed mechanism-of-action data from DrugBank.
- Hydroxyzine-specific trials or studies in urticaria. The only registered trial retrieved does not study hydroxyzine.
- A comparison against second-generation antihistamines, to define hydroxyzine's role, for example as an add-on or for nocturnal itch.

**Side note:** the third-ranked prediction, cold urticaria, has better direct support. It includes a 1984 randomized double-blind comparison that included hydroxyzine (PMID 6480953) and a completed Phase 4 study of 5 antihistamines in urticaria (NCT01940393). It may be worth evaluating separately.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

