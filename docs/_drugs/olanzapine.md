---
layout: default
title: Olanzapine
parent: 僅模型預測 (L5)
nav_order: 985
evidence_level: L5
indication_count: 3
---

# Olanzapine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Olanzapine: From Antipsychotic Use to Treatment-Resistant Panic Disorder with Agoraphobia

## One-Sentence Summary

Olanzapine is an atypical (second-generation) antipsychotic; this evidence pack does not include a specific original-indication text, but olanzapine is widely known for treating schizophrenia and bipolar disorder. TxGNN's highest-scoring prediction (benign paroxysmal torticollis of infancy) was reviewed and **rejected** as mechanistically implausible and potentially unsafe (see note below). Of the remaining candidates, **Agoraphobia** (in the context of treatment-resistant panic disorder) is the most credible, supported by **1 open-label trial** and **7 publications**, though all evidence remains observational/uncontrolled (L3).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (olanzapine is a known atypical antipsychotic; original_indications field was empty) |
| Predicted New Indication | Agoraphobia (treatment-resistant panic disorder, augmentation therapy) |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L3 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, olanzapine is part of the atypical (second-generation) antipsychotic class, with established efficacy in psychotic and mood disorders via combined 5-HT2A, D2, noradrenergic, and histaminergic receptor antagonism. Its FDA-approved combination with fluoxetine (Symbyax) for treatment-resistant depression and bipolar depression demonstrates that this multi-receptor profile can extend beyond core psychotic symptoms into mood and anxiety domains.

Agoraphobia is most often studied clinically as a comorbid feature of panic disorder rather than as an isolated diagnosis. The mechanistic rationale here is that olanzapine's sedative/anxiolytic properties support its use as an **augmentation agent** in SSRI-resistant panic disorder — a secondary, adjunctive mechanism rather than a primary anti-anxiety design target. This is a biologically plausible but indirect link, consistent with the L3 evidence tier assigned.

**Note on the top-ranked TxGNN candidate:** TxGNN's highest-scoring prediction for olanzapine was *benign paroxysmal torticollis of infancy* (score 99.54%, rank 11202). This candidate was reviewed and **rejected**: it is a self-limited, infancy-onset vestibular/vagal condition, and olanzapine (a D2/5-HT2A antagonist) is clinically known to *induce* extrapyramidal symptoms and acute dystonia — a mechanism that opposes, rather than supports, treatment of torticollis. The high TxGNN score likely reflects a knowledge-graph confound between "antipsychotic-induced movement disorder" and "antipsychotic-treats-movement-disorder" relationships. Antipsychotics are also not indicated in infants. This candidate is not carried forward in this report (decision stage S0, recommendation: Hold).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(One open-label trial (PMID 16415705) exists but is indexed as literature rather than a registered clinical trial record — see Literature Evidence below.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40946318](https://pubmed.ncbi.nlm.nih.gov/40946318/) | 2025 | Review | Psychotherapy and Psychosomatics | Systematic review of pharmacological, psychotherapeutic, and neurostimulatory options for treatment-resistant anxiety disorders |
| [26635099](https://pubmed.ncbi.nlm.nih.gov/26635099/) | 2016 | Review | Expert Opinion on Pharmacotherapy | Systematic review of treatment-resistant panic disorder; ~1/3 of patients have persistent symptoms despite standard therapy |
| [25012437](https://pubmed.ncbi.nlm.nih.gov/25012437/) | 2014 | Cohort | Journal of Affective Disorders | Comorbid agoraphobia/panic/OCD associated with worse 24-month outcomes in bipolar I disorder |
| [16415705](https://pubmed.ncbi.nlm.nih.gov/16415705/) | 2006 | Open-label Trial | Journal of Clinical Psychopharmacology | 12-week, fixed-dose (5 mg/d) olanzapine augmentation in 31 SSRI-resistant panic disorder patients with/without agoraphobia; showed efficacy signal |
| [17099612](https://pubmed.ncbi.nlm.nih.gov/17099612/) | 2006 | Case Report | Psychiatria Danubina | CBT-based treatment of panic disorder with agoraphobia comorbid with psychosis |
| [15470803](https://pubmed.ncbi.nlm.nih.gov/15470803/) | 2004 | Case Report | Pharmacopsychiatry | Olanzapine + paroxetine combination associated with full remission in refractory panic disorder |
| [10739446](https://pubmed.ncbi.nlm.nih.gov/10739446/) | 2000 | Case Report | American Journal of Psychiatry | Early case report describing olanzapine's effect on panic attacks |

---

## Safety Considerations

Please refer to the package insert for safety information.

**Data gap flagged as Blocking:** TFDA-equivalent label warnings/contraindications (DG001) have not yet been retrieved. This evidence pack notes that this gap currently **prevents completion of the initial safety screening (S1)** for any olanzapine repurposing candidate. Given olanzapine's known class-level risks (metabolic syndrome, weight gain, dyslipidemia, QT prolongation, extrapyramidal symptoms), a full label review is required before any clinical advancement.

---

## Additional TxGNN-Predicted Indication: Dysthymic Disorder

For completeness, TxGNN's third candidate (score 99.28%, rank 16083) — **Dysthymic Disorder** — is also L3/S1 ("Research Question") and worth noting alongside agoraphobia:

**Rationale:** Olanzapine's multi-receptor profile (5-HT2A, D2, NE, H1) is already leveraged in the FDA-approved olanzapine–fluoxetine combination (Symbyax) for treatment-resistant depression and bipolar depression. Extension to dysthymia (chronic low-grade depression) is mechanistically plausible as an augmentation strategy, but current evidence comes largely from comorbid populations (e.g., borderline personality disorder with dysthymia) in open-label studies, not dysthymia-specific controlled trials. The long-term metabolic risk profile warrants caution given the chronic nature of dysthymia treatment.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/) | 2010 | Review (Cochrane) | Cochrane Database of Systematic Reviews | Systematic review of second-generation antipsychotics as augmentation for MDD and dysthymia |
| [34727399](https://pubmed.ncbi.nlm.nih.gov/34727399/) | 2021 | Review | Human Psychopharmacology | Meta-analysis of amisulpride (related benzamide class) for depressive symptoms across psychiatric disorders |
| [11920152](https://pubmed.ncbi.nlm.nih.gov/11920152/) | 2002 | Review | Molecular Psychiatry | Reviews substituted benzamides' dual efficacy in dysthymia and schizophrenia negative symptoms, exploring shared mechanism |
| [22938165](https://pubmed.ncbi.nlm.nih.gov/22938165/) | 2012 | Review | Bipolar Disorders | Evidence-based options for treatment-resistant bipolar disorder, including antipsychotic augmentation |
| [10578457](https://pubmed.ncbi.nlm.nih.gov/10578457/) | 1999 | Open-label Trial | Biological Psychiatry | Open-label olanzapine trial in borderline personality disorder with comorbid dysthymia; safety/efficacy signal |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three TxGNN-predicted indications for olanzapine rely on L3-or-lower evidence (no completed RCTs), and the Blocking data gap on TFDA-equivalent label warnings (DG001) means the safety screening step (S1) cannot be formally completed for any candidate. The top-ranked prediction (torticollis of infancy) has been independently rejected as mechanistically implausible and unsafe.

**To proceed, the following is needed:**
- Retrieve TFDA/FDA label warnings and contraindications (DG001, Blocking) before any further scoring
- Confirm detailed mechanism of action (DG002) to strengthen mechanistic-link analysis
- For agoraphobia: seek controlled (RCT-level) data on olanzapine augmentation in SSRI-resistant panic disorder/agoraphobia, given only one small open-label trial (n=31) currently exists
- For dysthymic disorder: seek dysthymia-specific (rather than comorbid-population) controlled trial data
- Formal exclusion documentation for benign paroxysmal torticollis of infancy to prevent recurrence in future TxGNN re-scoring cycles
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

