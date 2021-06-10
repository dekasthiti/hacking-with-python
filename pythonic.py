from collections import defaultdict
import heapq
import functools


def compute_top_k_variance(students, scores, k):
    """
    Students and scores are equal length lists of strings and floats, respectively.
    The function computes for each string that appears at least k times in the list the variance of the top k scores
    that correspond to it. Strings that appear fewer than k times are not considered.
    """
    
    counts = {}
    # Lot of boilerplate code is non-pythonic
    if not pythonic:
        # First, count the scores a student has
        for i in range(len(students)):
            if students[i] not in counts:
                counts[students[i]] = 1
            else:
                counts[students[i]] += 1
                
        # If a student has more than k scores, initialize an empty list for that student
        all_scores = {}
        for key in counts:
            if counts[key] >= k:
                all_scores[key] = []
                
        # Accumulate the actual scores of the student
        for i in range(len(students)):
            if students[i] in all_scores:
                all_scores[students[i]].append(scores[i])

        # Now sort the scores of the student, and save the topk
        top_k_scores = {}
        for key in all_scores:
            sorted_scores = sorted(all_scores[key])
            top_k_scores[key] = []
            for i in range(k):
                top_k_scores[key].append(sorted_scores[len(sorted_scores) - 1 - i])

        # Calculate variance
        result = {}
        for key in top_k_scores:
            total = 0
            for score in top_k_scores[key]:
                total += score
            mean = total / k
            variance = 0
            for score in top_k_scores[key]:
                variance = variance + (score - mean) * (score - mean)
    
            result[key] = variance
            
    else:
        # Using defaultdict with initialized list
        all_scores = defaultdict(list)
        for student, score in zip(students, scores):
            all_scores[student].append(score)
        
        # Dictionary comprehension with conditional
        top_k_scores = {student: heapq.nlargest(k, scores) for student, scores in all_scores.items() if len(scores)
                        >= k}
        
        # This is pythonic, but just not readable to me
        if not readable:
            result = {
                student: functools.reduce(lambda variance, score: variance + (score - mean) ** 2, scores, 0)
                for student, scores, mean in
                (
                    (student, scores, sum(scores) / k)
                    for student, scores in top_k_scores.items()
                )
                }
        
        # This is pythonic and readable to me
        else:
            result = defaultdict(float)
            for student, scores in top_k_scores.items():
                mean = sum(scores) / k
                result[student] = functools.reduce(lambda variance, score: variance + (score - mean) ** 2, scores, 0)
            
    return result


if __name__ == '__main__':
    pythonic = True
    readable = True
    students = ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']
    scores = [10, 20, 30, 0, 5, 10, 30, 20, 30]
    k = 2
    result = compute_top_k_variance(students, scores, k)
    print(result)