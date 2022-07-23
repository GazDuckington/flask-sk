from functools import cache

from sqlalchemy import desc

from database.models import (
    Base,
    Likelihood,
    Prior,
    StopWords,
    Training,
    engine,
    session,
)


def createDb():
    """Create Database dataset.db"""
    Base.metadata.create_all(engine)


def insertTraining(txt: str, lbl: int):
    """Insert text and label into training table"""
    local_session = session(bind=engine)
    new_training = Training(text=txt, label=lbl)
    local_session.add(new_training)
    local_session.commit()


@cache
def readStopWords():
    """Read all stop words"""
    local_session = session(bind=engine)
    stops = local_session.query(StopWords).all()

    return {data.content for data in stops}


@cache
def readAllTraining():
    """Read all training dataset"""
    local_session = session(bind=engine)
    training = local_session.query(Training).yield_per(5).all()

    return {data.id: {"text": data.text, "label": data.label} for data in training}


@cache
def readLoglikelihood():
    """Read all loglikelihoods. Returns dictionary."""
    local_session = session(bind=engine)
    loglikelihood = local_session.query(Likelihood).all()

    return {data.text: data.loglikelihood for data in loglikelihood}


@cache
def readLogprior():
    """Read all logprior. Returns dictionary."""
    local_session = session(bind=engine)
    prior = local_session.query(Prior).order_by(desc(Prior.id)).first()

    return prior.logprior
