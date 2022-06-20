# Juncture

Juncture is a web service that renders interactive visual essays from plain text files.  

## Quick start

[Examples](examples)

## Content hosting

### Juncture-hosted content

### Hosting content in GitHub

# Juncture site hosting

As a hosted service Juncture can be used directly or as a back-end service to a self-managed web application.  This document provides an overview of the 

1. Juncture-managed content and hosting
2. Self-managed content and hosting

## Juncture as a hosted service

The simplest way to use Juncture is as a hosted service.  When using Juncture in this way visual essays and Juncture sites are served from the `juncture.digital.org` domain.  When using Juncture as a hosted service the visual essay source files may be managed by Juncture or self-hosted using a Github repository.

**Pros:**

  - No Cost
  - No setup and administration

**Cons:**

  - Non-custom domain

## Using a custom domain

If a custom domain is desired a self-hosted Juncture web application can be configured.  The Juncture web application can be configured for either static or server-based hosting.  The static hosting option is the easiest and least expensive option for a custom domain and may be a good choice for many users.  The main disadvantage of static hosting is that crawling by public search engines can often be suboptimal.  Server based hosting options are probably best when good Search Engine Optimization (SEO) is needed.  Good low-cost options are available for server based hosting.

### Static (client) hosting

This section describes 2 options for static hosting of Juncture site.  Many other options for static hosting are possible.  the 2 described below are free and easy to setup, are representative of other approaches that could be used.

- Pros:
  - Often free (not including domain registration)
- Cons:
  - Minor setup and administration required
  - Can have poor Search Engine Optimization (SEO)

#### GitHub Pages

In addition to its use as a site for managing visual essay source text files, GitHub also provides a static site hosting service.  This service is free to use and is easy to configure with a custom domain.

#### Netlify

[Netlify setup](netlify-setup)

### Server hosting

- Pros:
  - Good SEO
- Cons:
  - Generally involves recurring (often modest) hosting charges
  - Some setup and administration required

#### PythonAnywhere

[PythonAnywhere setup](pythonanywhere-setup)

#### Google Cloud

[Google Cloud Run setup](gcr-setup)

#### Amazon Web Services (AWS) {.aws}

[Amazon Web Services setup](aws-setup)
