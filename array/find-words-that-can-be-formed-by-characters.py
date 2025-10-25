class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        sum = 0
        for s in words:
          is_good = True
          chars_copy = chars
          for c in s:
            if c not in chars_copy:
              is_good = False
              break
            else:
              chars_copy = chars_copy.replace(c, '', 1)
          if is_good:
            sum += len(s)
        return sum
