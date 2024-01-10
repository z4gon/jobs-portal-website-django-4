from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

# Create your views here.

all_jobs = {
    1: {
        "id": 1,
        "title": "Python Developer",
        "company": "Google",
        "location": "Mountain View, CA"
    },
    2: {
        "id": 2,
        "title": "Java Developer",
        "company": "Facebook",
        "location": "Menlo Park, CA"
    },
    3: {
        "id": 3,
        "title": "Ruby Developer",
        "company": "Amazon",
        "location": "Seattle, WA"
    }
}

def jobs_list(request):
    jobs_html = [
        f"""
        <li>
            <h2>{job.get("title")}</h1>
            <h3>{job.get("company")}</h2>
            <p>{job.get("location")}</p>
            Visit <a href={reverse('job_detail', args=[job.get("id")])}>this link</a> for more info.
        </li>
        """ for job in all_jobs.values()
    ]

    return HttpResponse(f"""
        <h1>Jobs List</h1>
        <hr />
        <ul>
            {"".join(jobs_html)}
        </ul>
    """)

def job_detail(request, job_id):
    try:
        if job_id == 0:
            return redirect(reverse('jobs_list')) # redirect home

        job = all_jobs[job_id] # fails if not found
        url = reverse('job_detail', args=[job_id])
        
        return HttpResponse(f"""
            <h1>{job.get("title")}</h1>
            <h2>{job.get("company")}</h2>
            <p>{job.get("location")}</p>
            Visit <a href={url}>this link</a> for more info.
        """)
    
    except KeyError:
        return HttpResponseNotFound(f"""
            <h1>Job not found</h1>
            <p>Sorry, but the job you are looking for does not exist.</p>
        """)