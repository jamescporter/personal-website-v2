---
layout: page
title: Research
permalink: /research/
description: Retinal imaging, machine learning and neurodegenerative brain health.
nav: true
nav_order: 1
---

<link rel="stylesheet" href="{{ '/assets/css/research.css' | relative_url }}">

<div class="rs-page">
  <header class="rs-lead">
    <p class="rs-kicker">Precision medicine · Retinal imaging · Machine learning</p>
    <h2>Can a retinal photograph tell us something meaningful about brain health?</h2>
    <p class="rs-standfirst">My PhD research investigates whether information in colour photographs of the retina can help estimate retinal structure normally measured by optical coherence tomography (OCT), and how those estimates relate to neurodegenerative disease in population studies.</p>
    <div class="rs-actions">
      <a class="rs-primary-link" href="{{ '/publications/' | relative_url }}">Publications &amp; outputs <span aria-hidden="true">→</span></a>
      <a href="{{ '/cv/' | relative_url }}">Experience &amp; education <span aria-hidden="true">→</span></a>
    </div>
  </header>

  <section class="rs-section" id="research-question">
    <p class="rs-kicker">01 / Motivation</p>
    <h2>Why retinal imaging?</h2>
    <div class="rs-prose">
      <p>The retina is part of the central nervous system and can be examined non-invasively. OCT measures the thickness of individual retinal layers, while colour fundus photography (CFP) captures a two-dimensional image of the back of the eye. The two techniques provide different kinds of information, and fundus photography is more widely available in many settings.</p>
      <p>My research asks whether machine learning can extract useful, OCT-related structural information from CFP, and whether such estimates preserve associations between retinal measurements and later neurodegenerative outcomes. An association with future disease does not by itself establish a clinically useful screening test.</p>
    </div>
  </section>

  <section class="rs-section" id="research-approach">
    <p class="rs-kicker">02 / Research programme</p>
    <h2>From retinal images to interpretable evidence</h2>
    <div class="rs-steps">
      <article class="rs-step">
        <span class="rs-step-number">01</span>
        <div>
          <h3>Estimate retinal structure</h3>
          <p>Use paired CFP and OCT observations from UK Biobank to train models that estimate selected OCT-derived retinal layer thicknesses from fundus photographs. Foundation-model image representations, including RETFound, provide features for downstream estimation.</p>
        </div>
      </article>
      <article class="rs-step">
        <span class="rs-step-number">02</span>
        <div>
          <h3>Evaluate anatomical fidelity</h3>
          <p>Compare estimated measurements with OCT-measured thicknesses using held-out participants and appropriate error, agreement and calibration analyses. Accurate prediction, preservation of population variation and interchangeability with the original measurement are separate questions.</p>
        </div>
      </article>
      <article class="rs-step">
        <span class="rs-step-number">03</span>
        <div>
          <h3>Study disease associations</h3>
          <p>Investigate associations with incident dementia and Parkinson's disease through longitudinal survival analyses. Compare OCT-measured and CFP-estimated measurements, taking account of relevant clinical covariates and the distinction between association and predictive discrimination.</p>
        </div>
      </article>
    </div>
  </section>

  <section class="rs-section" id="methods">
    <p class="rs-kicker">03 / Methods</p>
    <h2>Methods &amp; research practice</h2>
    <div class="rs-methods">
      <div class="rs-method">
        <h3>Medical imaging</h3>
        <p>Colour fundus photography, OCT-derived retinal thicknesses, retinal image quality control and participant-level study design.</p>
      </div>
      <div class="rs-method">
        <h3>Machine learning</h3>
        <p>Pretrained retinal image representations, statistical regression, held-out evaluation and investigation of model calibration.</p>
      </div>
      <div class="rs-method">
        <h3>Longitudinal statistics</h3>
        <p>Cox proportional-hazards modelling, covariate adjustment, risk discrimination, bootstrap comparisons and sensitivity analyses.</p>
      </div>
      <div class="rs-method">
        <h3>Reproducible computing</h3>
        <p>Python and R workflows, data provenance, participant-disjoint validation and documented research software.</p>
      </div>
    </div>
  </section>

  <section class="rs-section" id="research-outputs">
    <p class="rs-kicker">04 / Selected outputs</p>
    <h2>Research outputs</h2>
    <div class="rs-output-list">
      <article class="rs-output">
        <span class="rs-output-meta">2025 · Published meeting abstract &amp; conference poster</span>
        <h3>Prediction of Optical Coherence Tomography Retinal Layer Thickness from Colour Fundus Photography in the UK Biobank</h3>
        <p>Porter, J. C., Bernabeu, M. O. &amp; Dhillon, B. An ARVO 2025 meeting abstract published in <em>Investigative Ophthalmology &amp; Visual Science</em>.</p>
        <a href="https://iovs.arvojournals.org/article.aspx?articleid=2810477">Read the published abstract <span aria-hidden="true">↗</span></a>
      </article>
      <article class="rs-output">
        <span class="rs-output-meta">2026 · Published research software</span>
        <h3>retfound-unofficial</h3>
        <p>An unofficial pip-installable distribution of the existing RETFound software for use in restricted research environments. The contribution concerns packaging and distribution, not development of the original RETFound foundation model.</p>
        <a href="https://doi.org/10.5281/zenodo.22129620">Software record and DOI <span aria-hidden="true">↗</span></a>
      </article>
    </div>
    <p class="rs-output-more"><a href="{{ '/publications/' | relative_url }}">All verified outputs and related links <span aria-hidden="true">→</span></a></p>
  </section>

  <aside class="rs-note" aria-label="Research status">
    <strong>Current work</strong>
    <p>A first-author manuscript examining estimated retinal thicknesses and neurodegenerative-disease associations is in preparation. Detailed findings will be shared through the relevant publication process; work in preparation is not presented here as peer-reviewed evidence.</p>
  </aside>

  <footer class="rs-footer">
    <p>This research is undertaken within the MRC-funded Precision Medicine CDT at the University of Edinburgh's Usher Institute and Centre for Medical Informatics, using approved access to UK Biobank data.</p>
    <a href="https://www.research.ed.ac.uk/en/persons/james-c-porter/">University of Edinburgh research profile <span aria-hidden="true">↗</span></a>
  </footer>
</div>
