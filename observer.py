# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Observer:
    _metaclass_ = ABCMeta

    @abstractmethod
    def onJobPosted(self): pass


class JobPost:
    _title = None

    def __init__(self, title):
        self._title = title

    def getTitle(self):
        return self._title


class JobSeeker(Observer):
    _name = None

    def __init__(self, name):
        self._name = name

    def onJobPosted(self, job):
        print("Hello,", self._name, "! The ", job.getTitle(), " job is available!")


class JobPosting(Observer):
    _observers = []

    def _notify(self, jobposting):
        for observer in self._observers:
            observer.onJobPosted(jobposting)

    def attach(self, observer):
        self._observers.append(observer)

    def addJob(self, jobposting):
        self._notify(jobposting)


jon = JobSeeker("John")
smit = JobSeeker("Smith")

jobposting = JobPosting()
jobposting.attach(jon)
jobposting.attach(smit)
jobposting.addJob(JobPost("New Programming"))