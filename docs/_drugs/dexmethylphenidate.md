---
layout: default
title: Dexmethylphenidate
parent: 僅模型預測 (L5)
nav_order: 595
evidence_level: L5
indication_count: 10
---

# Dexmethylphenidate
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

# Dexmethylphenidate: From ADHD to Specific Developmental Disorder

## One-Sentence Summary

Dexmethylphenidate is the pharmacologically active d-enantiomer of methylphenidate, a central nervous system stimulant established for ADHD treatment that works by inhibiting dopamine and norepinephrine reuptake transporters (DAT/NET).
The TxGNN model predicts it may be effective for **Specific Developmental Disorder**, with **1 clinical trial** currently providing indirect supporting evidence — no directly relevant published literature was identified.
The mechanistic rationale is biologically plausible given the high comorbidity between ADHD and neurodevelopmental/learning disorders, though formal evidence for this specific indication remains limited.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ADHD (attention deficit hyperactivity disorder) |
| Predicted New Indication | Specific Developmental Disorder |
| TxGNN Prediction Score | 99.9997% |
| Evidence Level | L3 |
| US Market Status | Not found in queried database |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Dexmethylphenidate exerts its effects through dual inhibition of the dopamine transporter (DAT) and norepinephrine transporter (NET), increasing monoamine availability in the prefrontal cortex. This enhances attention, cognitive flexibility, and working memory — the core executive functions that underpin both ADHD and a range of specific developmental disorders such as dyslexia and developmental language disorder.

The biological bridge between ADHD and specific developmental disorders is well-established. Under DSM-5 and ICD-11, both ADHD and specific developmental disorders (including specific learning disorders and developmental language disorder) are classified within the same overarching category of neurodevelopmental disorders. Comorbidity rates between these two conditions are notably high, estimated at 60–80%, suggesting shared underlying neurobiological substrates — particularly deficits in prefrontal-striatal circuits regulated by dopaminergic and noradrenergic signalling.

However, it is important to note that the available clinical trial evidence is indirect. The identified Phase 4 study examines methylphenidate/amphetamine use in children with autism spectrum disorder (ASD) comorbid with ADHD — a population that falls within the broader neurodevelopmental disorder umbrella, but is not equivalent to a specific learning or language developmental disorder. No clinical evidence directly targeting dexmethylphenidate as a treatment for specific developmental disorders as a primary indication has been identified, meaning the current support is mechanistic and inferential rather than direct.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05916339](https://clinicaltrials.gov/study/NCT05916339) | Phase 4 | Recruiting | 500 | Pragmatic SMART design trial comparing methylphenidate vs. amphetamine for ADHD management in children and adolescents with autism spectrum disorder; also evaluates the role of alpha-2 agonists as adjunct or alternative therapy |

> **Note:** This trial studies stimulant medications (including methylphenidate, the racemic parent compound of dexmethylphenidate) in ASD+ADHD populations. ASD falls within the ICD-11 category of neurodevelopmental disorders, which overlaps with specific developmental disorders. The evidence is indirect but provides important safety and effectiveness data relevant to this patient population.

---

## Literature Evidence

Currently no directly relevant literature available for dexmethylphenidate in specific developmental disorder.

---

## US Market Information

No authorizations found in the queried database for dexmethylphenidate.

> **Note:** This reflects the results of the automated database query. Dexmethylphenidate (Focalin®, Focalin XR®) has known FDA approvals for ADHD; verification against the current FDA Orange Book is recommended to reconcile this data gap.

---

## Safety Considerations

Safety data was not retrievable through the automated pipeline for this compound. Please refer to the package insert for complete warnings, contraindications, and precautions.

> Given that dexmethylphenidate is a Schedule II controlled CNS stimulant, key areas to verify from the prescribing information include: cardiovascular risk (hypertension, tachycardia), CNS effects (insomnia, anxiety, psychosis risk), contraindication in patients with known hypersensitivity to methylphenidate, and risks in patients with structural cardiac abnormalities or a personal/family history of psychosis.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link is biologically coherent — DAT/NET inhibition improves prefrontal executive function, which is deficient in both ADHD and specific developmental disorders, and comorbidity data strongly supports a shared neurobiological substrate. However, evidence is currently indirect (one Phase 4 trial in an overlapping but distinct population) with no published literature directly supporting this repurposing direction.

**To proceed, the following is needed:**

- **Safety data retrieval:** Download and parse the FDA package insert (or TFDA package insert if applicable) to complete the S1 safety screening — currently flagged as a blocking data gap
- **MOA confirmation:** Query DrugBank API for DB06701 to formally document mechanism of action, which is critical for the mechanistic linkage analysis
- **Direct clinical evidence:** Identify or design trials specifically targeting dexmethylphenidate (or methylphenidate) in specific developmental disorder subtypes (dyslexia, developmental language disorder, DCD) as primary indications — not solely as comorbid ADHD management
- **Subtype stratification:** Distinguish between specific learning disorder, developmental language disorder, and developmental coordination disorder, as the mechanistic rationale and likely benefit may differ substantially across subtypes
- **Regulatory status verification:** Reconcile the database gap by manually checking the FDA Orange Book for existing NDA approvals under dexmethylphenidate or methylphenidate d-isomer
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

