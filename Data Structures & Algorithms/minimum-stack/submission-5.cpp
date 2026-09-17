class MinStack {
public:
    stack<long long> st;
    long long min;
    MinStack() {
        
    }
    
    void push(int val) {
        if(st.empty()){
            st.push(0);
            min=val;
        }
        else{
            st.push(val-min);
            if(val<min) min=val;
        }
    }
    
    void pop() {
        if(st.empty()) return;

        long pop = st.top();
        st.pop();

        if (pop<0) min = min-pop;
    }
    
    int top() {
        long long encoded = st.top();

        if (encoded < 0) {
            return static_cast<int>(min);
        }

        return static_cast<int>(min +encoded);
    }
    
    int getMin() {
        return static_cast<int>(min);
    }
};
