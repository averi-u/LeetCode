class Solution {
public:
       int getTypeLeft(char c) {
      if (c == '(') return 1;
      else if (c == '[') return 2;
      else if (c == '{') return 3;
      else return -1;
    }
    int getTypeRight(char c) {
      if (c == ')') return 1;
      else if (c == ']') return 2;
      else if (c == '}') return 3;
      else return -1;      
    }

    bool isValid(string s) {
        stack<int> stk;
        for (int i = 0; i < s.size(); i++) {
          int LEFT_TYPE = getTypeLeft(s[i]);

          // right bracket
          if (LEFT_TYPE == -1) {
            if (stk.empty()) return false;
            int RIGHT_TYPE = getTypeRight(s[i]);
            if (RIGHT_TYPE == -1) return false;
            if (stk.top() != RIGHT_TYPE) return false;
            else stk.pop();
          // left bracket
          } else {
            stk.push(LEFT_TYPE);
          }
        }
        return stk.empty();
    }
};