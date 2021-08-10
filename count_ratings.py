from mrjob.job import MRJob
from mrjob.step import MRStep

class CountRatings (MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),
            MRStep(reducer=self.reducer_sort_by_rating_desc)
        ]

    def mapper(self, _, line):
        (user_id, movie_id, rating, timestamp) = line.split('\t')
        yield movie_id, 1

    def reducer(self, movie, ratings):
        yield None, (sum(ratings), movie)

    def reducer_sort_by_rating_desc(self, _, ratings):
        for count, key in sorted(ratings, reverse=True):
            yield (key, count)

if __name__ == '__main__':
    CountRatings.run()
