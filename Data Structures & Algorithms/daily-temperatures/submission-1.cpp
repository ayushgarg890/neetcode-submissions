class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        stack<pair<int,int>> st;
        vector<int> res(n,0);
        
        for(int i=n-1;i>=0;i--){
            while(!st.empty() && st.top().second<=temperatures[i]){
                st.pop();
            }

            if(!st.empty()){
                res[i] =st.top().first -i;
            }

            st.push({i,temperatures[i]});
        }

        return res;
    }
};
