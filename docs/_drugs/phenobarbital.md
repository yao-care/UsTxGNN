---
layout: default
title: Phenobarbital
parent: Model Prediction Only (L5)
nav_order: 1037
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
monitor_inn: "PHENOBARBITAL"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
description: "Phenobarbital: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Not recorded in the local data"
---

# Phenobarbital
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Phenobarbital: Trigeminal nerve neoplasm
{: .text-alpha }

## One-Sentence Summary

Phenobarbital is a long-established anticonvulsant, originally used for epilepsy (including generalized tonic-clonic and partial seizures) and headache disorders such as migraine and cluster headache.
The TxGNN model's top-ranked prediction is **Trigeminal Nerve Neoplasm**, but there are **0 clinical trials** and only **1 publication**, and that paper does not address this disease.
The prediction is best read as a likely model artifact. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 1) |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. From general pharmacology, phenobarbital is a barbiturate anticonvulsant that enhances GABA-A receptor-mediated inhibition. This explains its established role in seizure control.

For the top-ranked prediction, **trigeminal nerve neoplasm**, no credible mechanistic link can be established. Phenobarbital has no known antitumor activity. The only retrieved paper is a case series on Sturge-Weber syndrome, which is not a trigeminal neoplasm. The very high score (0.9996) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other predictions are more biologically coherent. Several are reflex or stimulus-triggered seizure syndromes (micturition-induced, eating, thinking, audiogenic, startle and reading seizures, plus orgasm-induced seizures). Phenobarbital's general antiseizure action makes these plausible, although direct evidence is scarce. **Trigeminal neuralgia** (score 0.9988) is also plausible, because anticonvulsants are the standard drug class, mainly carbamazepine. The evidence for phenobarbital itself is indirect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for trigeminal nerve neoplasm. No clinical trials were found for any of the other top 10 predicted indications either.

---

## Literature Evidence

For the top prediction, trigeminal nerve neoplasm:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | Anales espanoles de pediatria | Review of 14 Sturge-Weber syndrome cases over 25 years (clinical features, course, treatment response). Not a trigeminal neoplasm, so it is off-target. |

**Indirect evidence for other predicted indications (for context):**

| PMID | Year | Type | Journal | Relevant Indication | Key Findings |
|------|-----|------|------|------|---------|
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | Seizures (micturition-induced, indirect) | Levetiracetam vs phenobarbital for neonatal seizures. General seizure data only. |
| [37873971](https://pubmed.ncbi.nlm.nih.gov/37873971/) | 2023 | Systematic review | Cochrane Database Syst Rev | Seizures (indirect) | Anti-seizure medications for neonates with seizures. |
| [37655702](https://pubmed.ncbi.nlm.nih.gov/37655702/) | 2023 | Guideline | Epilepsia | Seizures (indirect) | ILAE recommendations on neonatal seizure management. |
| [24726506](https://pubmed.ncbi.nlm.nih.gov/24726506/) | 2014 | Case report | Seizure | Eating seizures | 50-year follow-up of a case of neonatal eating epilepsy. |
| [7259585](https://pubmed.ncbi.nlm.nih.gov/7259585/) | 1981 | Case report | Arquivos de neuro-psiquiatria | Eating seizures | Food-induced seizures; best result with valproate, clonazepam and phenobarbital combined. |
| [26690830](https://pubmed.ncbi.nlm.nih.gov/26690830/) | 2017 | Veterinary RCT | J Feline Med Surg | Audiogenic seizures | Levetiracetam vs phenobarbital in feline audiogenic reflex seizures. |
| [11129121](https://pubmed.ncbi.nlm.nih.gov/11129121/) | 2000 | Review | Drugs | Trigeminal neuralgia | Anticonvulsants in neuropathic pain syndromes. |
| [6264347](https://pubmed.ncbi.nlm.nih.gov/6264347/) | 1981 | Review | Neurology | Trigeminal neuralgia | In cats, carbamazepine, baclofen and phenytoin facilitated inhibition in the trigeminal nucleus, whereas phenobarbital usually depressed it. |

No literature was found for orgasm-induced seizures or beta-ketothiolase deficiency.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available | Phenobarbital (WINDER LABORATORIES, LLC) | Tablet | Not available (license status: cancelled) |

Phenobarbital is also recorded in oral tablet, injection and solution forms. The only US license in the compiled data is cancelled.

---

## Safety Considerations

**Knowledge-graph-derived contraindications** (not label text), grouped by category:
- **Liver and kidney:** liver failure, liver disease, kidney disease, gallbladder disease
- **Metabolic and haematological:** porphyria (inherited porphyria, porphyrin metabolism disease), thrombocytopenia, hyperglycaemia, hypothyroidism (including myxoedema and congenital hypothyroidism)
- **Respiratory and cardiovascular:** COPD, hypertension
- **Gastrointestinal:** gastric ulcer, peptic ulcer disease, gastritis
- **Psychiatric:** insomnia, anxiety disorder, neurotic disorder, dysthymic disorder, psychotic disorder, schizophreniform disorder, schizoaffective disorder, mental disorder
- **Autoimmune:** systemic lupus erythematosus (including paediatric)
- **Other:** pyoureter

**Drug interactions:** the query returned 100 interactions in total, and phenobarbital is a strong enzyme inducer. Examples of the 20 listed:
- **Major:** morphine (including liposomal), eliglustat, naldemedine, naloxegol, rolapitant
- **Moderate:** doxycycline, hydrocortisone, dexamethasone, prednisone, prednisolone, bupropion, aprepitant, metronidazole, pioglitazone, and others

**Safety signals in the literature:**
- Early barbiturate exposure caused audiogenic seizures and neuronal deficits in mice (PMID 7327097).
- Early phenobarbital treatment lowered IQ in toddlers with febrile seizures, with effects persisting at follow-up (PMID 10416094).
- Neonatal exposure caused neuronal apoptosis in rats (PMID 20618394).
- Anticonvulsant hypersensitivity syndrome is a risk (PMID 21658302).

Please refer to the package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, trigeminal nerve neoplasm, has no clinical trials, no relevant literature and no plausible mechanism (Evidence Level L5). The score looks like a TxGNN model (deep learning) artifact. Among the other predictions, the seizure-related ones have plausible mechanisms but only indirect evidence (L4), and trigeminal neuralgia is better served by established agents such as carbamazepine. The US licence is cancelled and the safety profile is substantial (many contraindications, strong CYP induction, neurodevelopmental concerns).

**To proceed, the following is needed:**
- Re-prioritise away from trigeminal nerve neoplasm. Consider the seizure-related and trigeminal neuralgia predictions as research questions instead.
- Retrieve the FDA package insert warnings and contraindications (currently a blocking gap).
- Obtain detailed mechanism of action data from DrugBank.
- Search for direct human evidence on reflex seizure syndromes, and for comparative data against first-line agents in trigeminal neuralgia.
- Assess neurodevelopmental, hepatic and drug interaction risks for any target population.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

