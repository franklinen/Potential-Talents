# Pipeline for Potential Talents Discovery
# Overview

The goal is to produce a pipeline for automating talent searches to spot potential candidates that could fit desired roles. The goal is to develop a machine learning-powered pipeline that could spot talented individuals, and rank them based on their fitness. The Machine learning pipeline takes in desired keywords to list and rank fitting candidates.

# Background and Motivation
For talent-sourcing companies, finding talented candidates is not easy, for several reasons. The first reason is one needs to understand what the role is very well to fill in that spot, this requires understanding the client’s needs and what they are looking for in a potential candidate. The second reason is one needs to understand what makes a candidate shine for the role we are in search for. Third, where to find talented individuals is another challenge.

The nature of the job requires a lot of human labor and is full of manual operations. Towards automating this process we want to build a better approach that could save time and finally help spot potential candidates that could fit the roles we are in search for. Moreover, going beyond that for a specific role we want to fill in we are interested in developing a machine learning-powered pipeline that could spot talented individuals, and rank them based on their fitness.

We are right now semi-automatically sourcing a few candidates, therefore the sourcing part is not a concern at this time but we expect to first determine the best matching candidates based on how fit these candidates are for a given role. We generally make these searches based on some keywords such as “full-stack software engineer”, “engineering manager” or “aspiring human resources” based on the role we are trying to fill in. These keywords might change, and you can expect that specific keywords will be provided to you.

Assuming that we were able to list and rank fitting candidates, we then employ a review procedure, as each candidate needs to be reviewed and then determined how good a fit they are through manual inspection. This procedure is done manually and at the end of this manual review, we might choose not the first fitting candidate in the list but maybe the 7th candidate in the list. If that happens, we are interested in being able to re-rank the previous list based on this information. This supervisory signal is going to be supplied by starring the 7th candidate in the list. Starring one candidate actually sets this candidate as an ideal candidate for the given role. Then, we expect the list to be re-ranked each time a candidate is starred.

# Datasets
The data comes from our sourcing efforts. I removed any field that could directly reveal personal details and gave a unique identifier for each candidate.

Attributes:
- id: unique identifier for candidate (numeric)

- job_title: job title for candidate (text)

- location: geographical location for candidate (text)

- connections: number of connections the candidate has, 500+ means over 500 (text)
  
# Practical Applications
-  Sourcing for applicants for job positions
-  Matching the right candidates from job applications
  
# Milestones
# References


