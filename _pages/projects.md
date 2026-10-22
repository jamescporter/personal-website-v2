---
layout: page
title: Portfolio
permalink: /portfolio/
description: Selected technical research projects, research software and computing work.
nav: true
nav_order: 2
---

My portfolio focuses on **problems I have worked on, methods I have implemented and software I have contributed to**. It complements the [research overview]({{ '/research/' | relative_url }}) and [publications]({{ '/publications/' | relative_url }}) rather than repeating a full CV.

<section class="site-section" id="retinal-imaging" aria-labelledby="retinal-imaging-title">
  <article class="site-record">
    <p class="site-meta">PhD research · Biomedical machine learning · Ongoing</p>
    <h2 id="retinal-imaging-title">Retinal imaging and neurodegenerative disease</h2>
    <p><strong>Problem:</strong> Optical coherence tomography (OCT) measures retinal structure, while colour fundus photographs are more readily available in many clinical and research settings. Can the information in a fundus photograph be used to estimate OCT-derived retinal thickness, and how should those estimates be interpreted in studies of neurodegenerative disease?</p>
    <p><strong>My contribution:</strong> Designed and implemented Python research workflows linking UK Biobank retinal images, OCT measurements and longitudinal health outcomes. The work covers participant-level data separation, image and segmentation quality control, model development and evaluation, survival analysis and sensitivity analyses.</p>
    <p><strong>Technical focus:</strong> Computer vision, pretrained retinal image representations, statistical regression, Cox proportional-hazards modelling, bootstrap inference and reproducible biomedical analysis.</p>
    <p><strong>Research status:</strong> An initial related study was presented at ARVO 2025 as a conference abstract and poster. A separate first-author manuscript is in preparation. The ongoing work is not presented as published or independently clinically validated, and restricted datasets and unpublished performance results are not shared here.</p>
    <div class="site-actions">
      <a href="{{ '/research/' | relative_url }}">Research approach</a>
      <a href="{{ '/publications/#meeting-abstract' | relative_url }}">2025 meeting abstract and poster</a>
      <a href="{{ '/cv/' | relative_url }}">Research experience</a>
    </div>
  </article>
</section>

<section class="site-section" id="retfound-packaging" aria-labelledby="retfound-project">
  <article class="site-record">
    <p class="site-meta">Research software · Public package · 2026</p>
    <h2 id="retfound-project">RETFound: unofficial Python packaging</h2>
    <p><strong>Problem:</strong> Using an existing retinal foundation model in a restricted research environment can be difficult when direct repository downloads or Git-based installations are unavailable.</p>
    <p><strong>My contribution:</strong> Created and maintain <code>retfound-unofficial</code>, a pip-installable distribution of the existing RETFound code. The package provides an installation route for the source modules and documents provenance, installation and usage. Pretrained model weights are <strong>not</strong> distributed with the package.</p>
    <p><strong>Technical focus:</strong> Python packaging, dependency management, software provenance and use of research software in restricted computing environments.</p>
    <p><strong>Attribution:</strong> This is an unofficial packaging and distribution contribution. The original model, architecture and underlying research belong to the upstream RETFound authors.</p>
    <div class="site-actions">
      <a href="https://github.com/jamescporter/Unofficial_RETFound_pip">Source and documentation</a>
      <a href="https://pypi.org/project/retfound-unofficial/">PyPI package</a>
      <a href="https://doi.org/10.5281/zenodo.22129620">Archived software DOI</a>
      <a href="https://github.com/rmaphoh/RETFound">Original RETFound</a>
    </div>
  </article>
</section>

<section class="site-section" id="extreme-classification" aria-labelledby="mach-project">
  <article class="site-record">
    <p class="site-meta">MSc dissertation · Machine learning research · 2018–2021</p>
    <h2 id="mach-project">Memory-efficient extreme classification</h2>
    <p><strong>Problem:</strong> Predictive tasks with very large numbers of possible labels can place substantial demands on model memory. My MSc Artificial Intelligence dissertation investigated how merged-averaged classifiers using hashing (MACH) behave under different data and model conditions.</p>
    <p><strong>My contribution:</strong> Implemented and evaluated hashing-based extreme-classification experiments, studying Count-Min Sketch variants and accuracy–memory trade-offs across benchmark datasets. The dissertation was undertaken in collaboration with Amazon Research.</p>
    <p><strong>Technical focus:</strong> Python, C++, TensorFlow, hashing, sketch-based algorithms, classification experiments and quantitative model comparisons.</p>
    <p><strong>Availability:</strong> This is a description of completed dissertation research, not a claim of a peer-reviewed publication or a currently available public source-code repository.</p>
    <div class="site-actions">
      <a href="{{ '/cv/#education' | relative_url }}">Education and dissertation context</a>
    </div>
  </article>
</section>

<section class="site-section" id="python-utilities" aria-labelledby="utilities-project">
  <article class="site-record">
    <p class="site-meta">Open-source contribution · Statistical Python utility</p>
    <h2 id="utilities-project">Practical descriptive statistics with Python</h2>
    <p><strong>Use case:</strong> During exploratory analysis, compact statistical summaries help identify unusual distributions and compare numerical columns.</p>
    <p><strong>Contribution:</strong> My public <code>super_describe_jcp</code> repository is a <strong>fork</strong> of <code>faseycranco/super_describe</code>, which provides a helper to summarise numeric columns of pandas DataFrames with measures such as mean, median, variation, skewness and kurtosis. I present it as a maintained or adapted utility, not wholly original research software.</p>
    <p><strong>Technical focus:</strong> Python, pandas and exploratory data analysis.</p>
    <div class="site-actions">
      <a href="https://github.com/jamescporter/super_describe_jcp">My public fork</a>
      <a href="https://github.com/faseycranco/super_describe">Upstream project</a>
    </div>
  </article>
</section>

<section class="site-section" aria-labelledby="more-professional-work">
  <h2 id="more-professional-work">More research and technical work</h2>
  <p>For verified research outputs, software records and additional public profiles, see [Publications]({{ '/publications/' | relative_url }}) and [Links &amp; Profiles]({{ '/links/' | relative_url }}). A full recruitment CV and restricted or unpublished research code are not hosted here.</p>
</section>
