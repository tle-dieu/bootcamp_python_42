class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        return (sum(coef * len(word) for coef, word in zip(coefs, words))
                if len(words) == len(coefs) else -1)

    @staticmethod
    def enumerate_evaluate(coefs, words):
        return (sum(coefs[i] * len(word) for i, word in enumerate(words))
                if len(words) == len(coefs) else -1)


WORDS = ["Le", "Lorem", "Ipsum", "est", "simple"]
COEFS = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(COEFS, WORDS))
WORDS = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
COEFS = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
print(Evaluator.enumerate_evaluate(COEFS, WORDS))
WORDS = ["Le", "Lorem", "Ipsum", "est", "simple"]
COEFS = [0.0, -1.0, 1.0, -12.0, 0.0]
print(Evaluator.enumerate_evaluate(COEFS, WORDS))
