# DevOps Digest — 2026-10-26

> Cybersecurity · AI News & Tools · DevSecOps · SRE
> Generated 2026-10-26 04:17 UTC

## 🛡️ Cybersecurity

### 1. [CISA Adds Six Known Exploited Vulnerabilities to Catalog](https://www.cisa.gov/news-events/alerts/2026/10/20/cisa-adds-six-known-exploited-vulnerabilities-catalog)
*CISA Advisories* · 2026-10-20

CISA has added six new vulnerabilities to its Known Exploited Vulnerabilities (KEV) Catalog , based on evidence of active exploitation. CVE-2026-96652 Plex Media Server Server-Side Request Forgery (SSRF) Vulnerability CVE-2026-96654 Plex Media Server Improper Neutralization of Encoded URI Schemes in a Web Page Vulnerability CVE-2026-96655 Plex Media Server Server-Side Request Forgery (SSRF) Vulnerability CVE-2026-96656 Plex Media Server External Control of File Name or Path Vulnerability CVE-2026-106931 EG Secure Solutions SiteGuard Server Edition OS Command Injection Vulnerability CVE-2026-110936 Siemens Software Center Uncontrolled Search Path Element Vulnerability These types of vulnerabilities are a frequent attack vector for malicious cyber actors and pose significant risks to the federal enterprise.

**LinkedIn angle:** If you own security posture, this is worth a 2-minute read.

<sub>matched: cisa, cve-, vulnerabilities, vulnerability</sub>

### 2. [Responding to core PHP vulnerabilities CVE-2026-109618 and CVE-2026-109619](https://cloud.google.com/blog/products/identity-security/responding-to-core-php-vulnerabilities-cve-2026-109618-cve-2026-109619/)
*Google Cloud Blog* · 2026-10-21

While Google Cloud itself is not vulnerable, users of PHP running on Google Cloud may be vulnerable . On Oct.

**LinkedIn angle:** Security teams: here's what this means for your threat model.

<sub>matched: cve-, exploit, gemini, vulnerabilities, vulnerability</sub>

### 3. [CISA Flags Two Actively Exploited Critical Flaws in Collabora Online and Arista VeloCloud](https://thehackernews.com/2026/10/cisa-flags-two-actively-exploited.html)
*The Hacker News* · 2026-10-24

Cybersecurity and Infrastructure Security Agency (CISA) on Friday added two vulnerabilities impacting Collabora Online Built-in CODE Server and Arista VeloCloud Orchestrator (VCO) to its Known Exploited Vulnerabilities (KEV), citing reports of active exploitation in the wild. The critical-severity vulnerabilities are listed below - CVE-2026-110447 (CVSS score: 9.2) - An operating

**LinkedIn angle:** A reminder that the attack surface keeps shifting — here's the takeaway.

<sub>matched: cisa, cve-, cvss, vulnerabilities</sub>

### 4. [Russia-Linked Hackers Used New Mesh Network Backdoor in Destructive Ukraine Attack](https://thehackernews.com/2026/10/russian-linked-hackers-used-new-mesh.html)
*The Hacker News* · 2026-10-23

The Russian state-sponsored hacking group Sandworm teamed up with another threat actor to carry out a destructive wiping attack targeting a Ukrainian logistics company last year. According to ESET, the attack involved UAC-0099 (aka Earth Sirrush) obtaining initial access to the target on July 16, 2025, via a spear-phishing email bearing a malware-laced attachment that led to the deployment of

**LinkedIn angle:** If you own security posture, this is worth a 2-minute read.

<sub>matched: backdoor, malware, phishing, threat actor</sub>

### 5. [Researchers Demonstrate Node2Shell RCE Exploit on Node.js Build Using Crafted Brotli Data](https://thehackernews.com/2026/10/researchers-demonstrate-node2shell-rce.html)
*The Hacker News* · 2026-10-23

Malicious Brotli data can make an application on an official build of Node.js run attacker-supplied code, security researchers at Imperva have demonstrated. Their "Node2Shell" proof of concept ran code on the official Node.js 24.22.0 image for Linux arm64, with no debugger or custom build, by feeding crafted data to the bundled Brotli decoder (CVE-2026-111497).

**LinkedIn angle:** A reminder that the attack surface keeps shifting — here's the takeaway.

<sub>matched: cve-, exploit, rce</sub>

## 🤖 AI News & Tools

### 1. [OpenAI and Anthropic cut their LLM prices by up to 80% within a few months. Why?](https://minimaxir.com/2026/10/cheap-llms/)
*Hacker News* · 2026-10-25 · 208 pts

OpenAI and Anthropic cut their LLM prices by up to 80% within a few months. Why?

**LinkedIn angle:** The AI tooling landscape moved again — here's why it matters for builders.

<sub>matched: anthropic, llm, openai</sub>

### 2. [Introducing Kimi K3.1 Pro](https://simonwillison.net/2026/Oct/23/kimi-k31-pro/)
*Simon Willison* · 2026-10-23

Introducing Kimi K3.1 Pro landed on the Kimi API today - it's not yet open weights, but Moonshot promise "Full model weights will be released by Nov 4, 2026". Artificial Analysis scored Kimi at 55 - ahead of Claude Fable 5.1, GPT-6 Astra, and Gemini 4 Argon (all at 53) and behind only Claude Opus 5.5 (58).

**LinkedIn angle:** Worth bookmarking if you're wiring AI into real workflows.

<sub>matched: claude, gemini, gpt, llm, openai</sub>

### 3. [Inside Agent Compute Engine: Building the compute foundation for the agentic era](https://cloud.google.com/blog/topics/ai-infrastructure/agent-compute-engine-deep-dive/)
*Google Cloud Blog* · 2026-10-22

Every decade or so, a shift in software forces us to rethink computer architecture from first principles. In a remarkably short span of time, agentic workloads have grown into one of the fastest-expanding consumers of compute and storage across

**LinkedIn angle:** Worth bookmarking if you're wiring AI into real workflows.

<sub>matched: agent, agentic</sub>

### 4. [ZenteiQ scales batch inference 4x with GKE Inference Gateway powered by llm-d](https://cloud.google.com/blog/products/containers-kubernetes/zenteiq-scales-physical-ai-inference-4x-with-gke-and-llm-d/)
*Google Cloud Blog* · 2026-10-21

To pre-train models that understand physical laws, governing equations, and numerical solvers, ZenteiQ designed and built a large-scale batch synthetic data-generation pipeline that runs across multiple model families and feeds verified datasets into training runs. At ZenteiQ, we are building sovereign scientific foundation models from scratch that interpret sim

**LinkedIn angle:** Another signal that the way we ship software is changing.

<sub>matched: inference, llm, pipeline</sub>

### 5. [The Harness Is the Hard Part of Agentic Pentesting](https://thehackernews.com/2026/10/the-harness-is-hard-part-of-agentic.html)
*The Hacker News* · 2026-10-21

Sure, the model writes the attacks. But everything that makes those attacks safe to run against production and worth acting on afterward lives in the harness around the model.

**LinkedIn angle:** Worth bookmarking if you're wiring AI into real workflows.

<sub>matched: agent, agentic, hugging face, openai</sub>

## 🔐 DevSecOps

### 1. [Is Kubernetes ready for AI agents?](https://thenewstack.io/kubernetes-ready-ai-agents/)
*The New Stack* · 2026-10-25

Kubernetes was built around a fairly simple assumption. appeared first on The New Stack .

**LinkedIn angle:** Shifting security left isn't a slogan — this is what it looks like in practice.

### 2. [Before you expand your GPU pool, measure the outcome](https://thenewstack.io/optimize-kubernetes-gpu-pools/)
*The New Stack* · 2026-10-24

For teams running AI workloads on Kubernetes, a fully allocated GPU pool and a growing batch-job queue might make expanding The post Before you expand your GPU pool, measure the outcome appeared first on The New Stack .

**LinkedIn angle:** Supply-chain and IaC security keep maturing. Here's the practical angle.

### 3. [Leaked LiteLLM Master Key Let Attackers Steal GitHub Tokens and Hijack Release Pipeline](https://thehackernews.com/2026/10/leaked-litellm-master-key-let-attackers.html)
*The Hacker News* · 2026-10-24

LiteLLM on Friday revealed that an Agent Platform master key accidentally published to a public GitHub repository in late May 2026 ultimately allowed the threat actor to push a malicious version of the popular Python package. "On May 27, 2026, a configuration file was committed to the public LiteLLM-Labs/lite-harness repository which inadvertently contained the master key to a deployment of

**LinkedIn angle:** Supply-chain and IaC security keep maturing. Here's the practical angle.

<sub>matched: agent, pipeline, threat actor</sub>

### 4. [How to Use Python UDF Logging for Pipeline Observability](https://cloud.google.com/blog/products/data-analytics/python-udf-logging-for-pipeline-observability-in-bigquery/)
*Google Cloud Blog* · 2026-10-19

We are announcing a new logging feature that is now available in Python User-Defined Function (UDF) in BigQuery. In this post, we’ll show you how to get started with Python UDF logging and walk through an e-commerce event ingestion pipeline as a practical, end-to-end example.

**LinkedIn angle:** Shifting security left isn't a slogan — this is what it looks like in practice.

<sub>matched: observability, pipeline</sub>

### 5. [Vercel sets a deadline for vendors to move beyond long-lived keys](https://thenewstack.io/vercel-oidc-static-credentials/)
*The New Stack* · 2026-10-23

Vercel wants to eliminate long-lived API keys from its ecosystem. It is giving Marketplace vendors until January 2027 to offer The post Vercel sets a deadline for vendors to move beyond long-lived keys appeared first on The New Stack .

**LinkedIn angle:** For anyone hardening their pipeline, there's a concrete lesson here.

## 📈 SRE / Reliability

### 1. [What does AI-assisted incident investigation actually look like at your company right now?](https://www.reddit.com/r/sre/comments/1xdcnyd/what_does_aiassisted_incident_investigation/)
*r/sre* · 2026-10-23

It'd help if you mention your stack (Datadog, Grafana, other) Thanks! submitted by /u/Commercial_Plastic72 [link] [comments]

**LinkedIn angle:** Directly relevant to Datadog work — a strong hook for a post tying this to real-world Datadog experience.

<sub>matched: datadog, grafana, incident</sub>

### 2. [Where do you put trace context when a queue envelope drops the headers?](https://www.reddit.com/r/sre/comments/1xegqso/where_do_you_put_trace_context_when_a_queue/)
*r/sre* · 2026-10-24

About 18000 runs cross an SQS queue, and 5400 of those arrive at the worker without their parent trace. End to end p95 latency is 8.2 seconds while the model span shows 1.9 seconds, leaving over 6 seconds of queue and worker time invisible in the trace.

**LinkedIn angle:** Reliability is a feature. Here's a pattern worth stealing.

<sub>matched: agent, incident, latency, opentelemetry, tracing</sub>

### 3. [Active incident at Dreamhost forcing password reset](https://www.dreamhoststatus.com/)
*Hacker News* · 2026-10-25 · 132 pts

Active incident at Dreamhost forcing password reset

**LinkedIn angle:** For the on-call crowd: a useful take on keeping systems healthy.

<sub>matched: incident</sub>

### 4. [How do I validate my autonomous SRE agent against real live data? My simulator-only evals have hit their limit seeking guidance](https://www.reddit.com/r/sre/comments/1xa5oge/how_do_i_validate_my_autonomous_sre_agent_against/)
*r/sre* · 2026-10-19

Live data streams continuously — do I need to pause/window it, or is manually triggering incidents (like I do in sim) the correct pattern against live data? And how do alerts even fire on real/replayed data?

**LinkedIn angle:** Reliability is a feature. Here's a pattern worth stealing.

<sub>matched: agent, incident, mcp, prometheus, sre</sub>

### 5. [Open to contribute to start-ups as DevOps/SRE or even Python part-time](https://www.reddit.com/r/sre/comments/1xfc3e4/open_to_contribute_to_startups_as_devopssre_or/)
*r/sre* · 2026-10-25

I feel I know Azure and GCP well but would like to test it out end to end (cause you don't know unless you do it yourself). Let me know if it resonates with you.

**LinkedIn angle:** Observability and SLOs done right — a quick field note.

<sub>matched: availability, sre</sub>


---
*20 items · DevOps Digest*