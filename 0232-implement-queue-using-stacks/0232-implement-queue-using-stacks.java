class MyQueue {
    ArrayList<Integer> que;

    public MyQueue() {
        que=new ArrayList<Integer>();
    }
    
    public void push(int x) {
       this.que.add(0,x);
    }
    
    public int pop() {
      return  this.que.remove(this.que.size()-1); 
    }
    
    public int peek() {
      return  this.que.get(this.que.size()-1); 
    }
    
    public boolean empty() {
      return this.que.size()==0;   
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */