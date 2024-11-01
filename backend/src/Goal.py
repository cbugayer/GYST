from pydantic import BaseModel, TypeAdapter, conint, conlist
from datetime import datetime, date
from Metric import Metric

class Goal(BaseModel):
    goal_id: int
    title: str
    description: str
    reason: str
    deadline: date
    metric: Metric
    priority: conint(ge=1, le=5)
    completed: bool
    created_at: datetime
    updated_at: conlist(datetime, min_length=1)

    def __repr__(self):
        return f"Goal(goal_id={self.goal_id}, title={self.title}, description={self.description}, reason={self.reason}, deadline={self.deadline}, metric={self.metric}, priority={self.priority}, completed={self.completed}, created_at={self.created_at}, updated_at={self.updated_at})"
    
    def __str__(self):
        return f"Goal(\
        \n  goal_id={self.goal_id},\
        \n  title={self.title},\
        \n  description={self.description},\
        \n  reason={self.reason},\
        \n  deadline={self.deadline.strftime('%m/%d/%Y')},\
        \n  metric={self.metric.value},\
        \n  priority={self.priority},\
        \n  completed={self.completed},\
        \n  created_at={self.created_at.strftime('%m/%d/%Y, %H:%M:%S')},\
        \n  updated_at={[dt.strftime('%m/%d/%Y, %H:%M:%S') for dt in self.updated_at]}\n)"
    
my_test_goal = Goal(goal_id=1, title="Test Goal", description="This is a test goal", reason="To test the Goal class", metric=Metric.percentage, deadline=date(2021, 12, 31), priority=3, completed=False, created_at=datetime.now(), updated_at=[datetime.now()])
print(my_test_goal)
