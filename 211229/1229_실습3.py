class Grade :
    def __init__ (self):
        info = input()
        info = info.split()
        self.name = info[0]
        self.score = info[1:]
        self.avg = self.calc_avg()
        self.grade = self.calc_grade()

    def calc_avg (self) :
        sum = 0
        for x in self.score :
            sum += int(x)
        return sum / len(self.score)
        

    def calc_grade (self) :
        if self.avg >= 90 :
            return 'A'
        elif self.avg >= 80 :
            return 'B'
        elif self.avg >= 70 :
            return 'C'
        else :
            return 'D'

    def __str__ (self) :
        return "%s의 평균은 %.2f로, %c 등급입니다.\n" %(self.name, self.avg, self.grade)


student = Grade()
print(student)
