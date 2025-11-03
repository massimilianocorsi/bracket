from sqlalchemy import Column, Integer, ForeignKey
from .base import Base  # Usare il base corretto in base alla struttura

class GoalScorer(Base):
    __tablename__ = 'goal_scorers'
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey('matches.id'))
    player_id = Column(Integer, ForeignKey('players.id'))
    minute = Column(Integer, nullable=True)
