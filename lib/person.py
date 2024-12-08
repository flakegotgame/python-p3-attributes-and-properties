#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin", "Customer Service", "Human Resources", "ITC", "Production",
    "Legal", "Finance", "Sales", "General Management", "Research & Development",
    "Marketing", "Purchasing"
]

class Person:
    def __init__(self, name="Guido", job="Sales"):
        self.set_name(name)
        self.set_job(job)

    def set_name(self, name):
        if isinstance(name, str) and (1 <= len(name) <= 25):
            self._name = name.title()  
        else:
            print("Name must be a string between 1 and 25 characters.")

    def set_job(self, job):
        if job.title() in APPROVED_JOBS:
            self._job = job.title()  
        else:
            print("Job must be in the list of approved jobs.")

    @property
    def name(self):
        return self._name

    @property
    def job(self):
        return self._job

