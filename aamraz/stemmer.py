import re


class Stemmer:
    """
    Stemmer class supporting both simple stemming and Porter Snowball stemming methods for Kurdish language.
    """

    def __init__(self, method='simple'):
        self.method = method

        # Define Kurdish-specific suffixes (examples; adjust as needed)
        self.plural_suffixes = ["ان", "ەکان", "یان", "یەکان"]
        self.comparative_suffixes = ["تر", "ترین"]
        self.adjectival_adverbial_suffixes = ["انە"]
        self.possessive_suffixes = ["یان", "تان", "مان", "ی"]

        # Define Porter Snowball suffix phases for Kurdish
        self.suffixes_phase_1 = self.plural_suffixes
        self.suffixes_phase_2 = self.comparative_suffixes
        self.suffixes_phase_3 = self.adjectival_adverbial_suffixes
        self.suffixes_phase_4 = self.possessive_suffixes

    def is_vowel(self, letter):
        """
        Check if a letter is a vowel in Kurdish.
        """
        vowels = ['ا', 'ە', 'ۆ', 'و', 'ی', 'ێ']
        return letter in vowels

    def is_consonant(self, letter):
        """
        Check if a letter is a consonant in Kurdish.
        """
        return not self.is_vowel(letter)

    def measure_m(self, word):
        """
        Measure the 'm' value, which is the number of vowel-consonant pairs.
        """
        vc_sequence = ""
        for i, letter in enumerate(word):
            if self.is_vowel(letter):
                vc_sequence += "V"
            else:
                vc_sequence += "C"
        # Count the VC pairs
        return vc_sequence.count("VC")

    def apply_suffix_rule(self, word, suffixes):
        """
        Apply suffix removal rules if the word ends with any of the given suffixes.
        """
        for suffix in suffixes:
            if word.endswith(suffix):
                base = word[:-len(suffix)]
                if self.measure_m(base) > 0:
                    return base
        return word

    def porter_snowball_step_1(self, word):
        """
        Step 1: Remove common plural suffixes (Porter Snowball logic).
        """
        return self.apply_suffix_rule(word, self.suffixes_phase_1)

    def porter_snowball_step_2(self, word):
        """
        Step 2: Remove comparative suffixes (Porter Snowball logic).
        """
        return self.apply_suffix_rule(word, self.suffixes_phase_2)

    def porter_snowball_step_3(self, word):
        """
        Step 3: Remove adjectival and adverbial suffixes (Porter Snowball logic).
        """
        return self.apply_suffix_rule(word, self.suffixes_phase_3)

    def porter_snowball_step_4(self, word):
        """
        Step 4: Remove possessive suffixes (Porter Snowball logic).
        """
        return self.apply_suffix_rule(word, self.suffixes_phase_4)

    def porter_snowball_stem(self, word):
        """
        Apply the full Porter Snowball stemming process through all steps.
        """
        word = self.porter_snowball_step_1(word)
        word = self.porter_snowball_step_2(word)
        word = self.porter_snowball_step_3(word)
        word = self.porter_snowball_step_4(word)
        return word

    def simple_stem(self, word):
        """
        Simple rule-based stemming method for Kurdish.
        """
        for suffix in self.plural_suffixes:
            if word.endswith(suffix):
                word = word[:-len(suffix)]

        for suffix in self.comparative_suffixes:
            if word.endswith(suffix):
                word = word[:-len(suffix)]

        for suffix in self.adjectival_adverbial_suffixes:
            if word.endswith(suffix):
                word = word[:-len(suffix)]

        for suffix in self.possessive_suffixes:
            if word.endswith(suffix):
                word = word[:-len(suffix)]

        return word

    def stem(self, word):
        """
        Apply stemming based on the selected method.
        """
        if self.method == 'simple':
            return self.simple_stem(word)
        elif self.method == 'porter_snowball':
            return self.porter_snowball_stem(word)
        else:
            raise ValueError(f"Stemming method '{self.method}' not recognized.")


