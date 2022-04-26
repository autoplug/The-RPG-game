class Course:
    def __init__(self, name, difficulty, points=0, topic="Business"):
        self.name = name
        self.difficulty = difficulty
        self.points = points
        self.topic = topic

    def compete_task(self, number_of_tasks):
        if number_of_tasks > 10:
            print('You must be cheating')
        elif number_of_tasks > 5:
            self.points += 2 * number_of_tasks
        else:
            self.points += number_of_tasks


class IntensiveCourse(Course):
    def __init__(self, name, difficulty):
        super().__init__(name, difficulty)

    def compete_task(self, number_of_tasks):
        self.points += 2 * number_of_tasks


class PartTimeCourse(Course):
    def __init__(self, name, difficulty, points):
        super().__init__(name, difficulty, points)


intensive_course = IntensiveCourse("Banking", 10)
part_time_course = PartTimeCourse("Cooking", 3, 2)
intensive_course.compete_task(40)
intensive_course.compete_task(6)
intensive_course.compete_task(2)
part_time_course.compete_task(40)
part_time_course.compete_task(6)
part_time_course.compete_task(2)
print(intensive_course.points)
print(part_time_course.points)
