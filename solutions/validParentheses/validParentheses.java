import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;

public class validParentheses {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	String input = "{([])[]{}}";
	System.out.println(valid(input));
    }

    public static boolean valid(String s) {
	String startState = "s";
	String acceptState = "h";
	HashSet<String> setOfStates = new HashSet<String>(Arrays.asList("a", "b", "c", "d", "e", "f", "g", "h", "s"));
	ArrayList<String[]> transition = new ArrayList<>();

	// skip all checked char
	transition.add(new String[] { "s", "X", "X", "R", "s" });
	transition.add(new String[] { "s", "Y", "Y", "R", "s" });
	transition.add(new String[] { "s", "Z", "Z", "R", "s" });
	// check if there are any open parentheses left
	transition.add(new String[] { "s", "*", "*", "L", "g" });
	transition.add(new String[] { "g", "X", "X", "L", "g" });
	transition.add(new String[] { "g", "Y", "Y", "L", "g" });
	transition.add(new String[] { "g", "Z", "Z", "L", "g" });
	transition.add(new String[] { "g", "*", "*", "R", "h" });
	// check ()
	transition.add(new String[] { "s", "(", "(", "R", "a" });
	transition.add(new String[] { "a", "(", "(", "R", "a" });
	transition.add(new String[] { "a", ")", "X", "L", "b" });
	transition.add(new String[] { "b", "X", "X", "L", "b" });
	transition.add(new String[] { "b", "Y", "Y", "L", "b" });
	transition.add(new String[] { "b", "Z", "Z", "L", "b" });
	transition.add(new String[] { "b", "(", "X", "R", "s" });
	transition.add(new String[] { "s", ")", "X", "L", "b" });
	// check []
	transition.add(new String[] { "s", "[", "[", "R", "c" });
	transition.add(new String[] { "c", "[", "[", "R", "c" });
	transition.add(new String[] { "c", "]", "Y", "L", "d" });
	transition.add(new String[] { "d", "X", "X", "L", "d" });
	transition.add(new String[] { "d", "Y", "Y", "L", "d" });
	transition.add(new String[] { "d", "Z", "Z", "L", "d" });
	transition.add(new String[] { "d", "[", "Y", "R", "s" });
	transition.add(new String[] { "s", "]", "Y", "L", "d" });
	// check {}
	transition.add(new String[] { "s", "{", "{", "R", "e" });
	transition.add(new String[] { "e", "{", "{", "R", "e" });
	transition.add(new String[] { "e", "}", "Z", "L", "f" });
	transition.add(new String[] { "f", "X", "X", "L", "f" });
	transition.add(new String[] { "f", "Y", "Y", "L", "f" });
	transition.add(new String[] { "f", "Z", "Z", "L", "f" });
	transition.add(new String[] { "f", "{", "Z", "R", "s" });
	transition.add(new String[] { "s", "}", "Z", "L", "f" });
	// transition from ( to [ or {
	transition.add(new String[] { "a", "[", "[", "R", "c" });
	transition.add(new String[] { "a", "{", "{", "R", "e" });
	// transition from [ to ( or {
	transition.add(new String[] { "c", "(", "(", "R", "a" });
	transition.add(new String[] { "c", "{", "{", "R", "e" });
	// transition from { to ( or [
	transition.add(new String[] { "e", "(", "(", "R", "a" });
	transition.add(new String[] { "e", "[", "[", "R", "c" });

	TuringMachine tm = new TuringMachine(setOfStates, startState, acceptState, transition);
	String input = "*" + s + "*";
	return tm.check(input);
    }
}

class TuringMachine {

    String input;
    HashSet<String> setOfStates;
    String startState;
    String acceptState;
    ArrayList<String[]> transition;
    HashMap<String, Node> map = new HashMap<>();

    TuringMachine(HashSet<String> setOfStates, String startState, String acceptState, ArrayList<String[]> transition) {
	this.setOfStates = setOfStates;
	this.startState = startState;
	this.acceptState = acceptState;
	this.transition = transition;

	// construct TM
	for (String stateName : this.setOfStates) {
	    if (stateName.equals(this.acceptState)) {
		Node node = new Node(stateName);
		node.changeToAcceptState();
		this.map.put(stateName, node);
	    } else {
		this.map.put(stateName, new Node(stateName));
	    }
	}

	for (int trans = 0; trans < transition.size(); trans++) {
	    String[] t = transition.get(trans);

	    // trans: [q0, 0, 0, R, q0]
	    Node fromNode = this.map.get(t[0]);
	    Node toNode = this.map.get(t[4]);

	    Edge edge = new Edge(t, toNode);
	    fromNode.addEdge(edge);
	}

    }

    boolean check(String input) {
	StringBuilder inputSB = new StringBuilder(input);

	Node curr = this.map.get(this.startState);

	int idx = 0;
	// read all leading * at the input
	while (inputSB.charAt(idx) == '*') {
	    idx += 1;
	}

	while (curr.isAcceptState == false && (idx <= inputSB.length() && idx >= 0)) {
	    String readVal = String.valueOf(inputSB.charAt(idx));
	    boolean found = false;
	    for (int i = 0; i < curr.edges.size(); i++) {
		// if read value is equal to given c, go to pointsTo state
		if (curr.edges.get(i).trans[1].equals(readVal)) {
		    found = true;
		    String change2Val = curr.edges.get(i).trans[2];
		    inputSB.setCharAt(idx, change2Val.charAt(0));
		    if (idx == inputSB.length() - 1) {
			inputSB.append("*");
		    } else if (idx == 0) {
			inputSB.insert(0, "*");
			idx += 1;
		    }
		    String direction = curr.edges.get(i).trans[3];
		    curr = curr.goToNext(readVal);
		    if (curr == null) {
			return false;
		    }
		    if (direction.equals("L")) {
			idx--;
		    } else if (direction.equals("R")) {
			idx++;
		    }
		    break;
		}
	    }
	    if (found == false) {
		return false;
	    }
	}

	return curr.isAcceptState;
    }

    String run(String input) {
	StringBuilder inputSB = new StringBuilder(input);

	Node curr = this.map.get(this.startState);

	int idx = 0;
	// read all leading * at the input
	while (inputSB.charAt(idx) == '*') {
	    idx += 1;
	}

	while (curr.isAcceptState == false && (idx <= inputSB.length() && idx >= 0)) {
	    String readVal = String.valueOf(inputSB.charAt(idx));
	    boolean found = false;
	    for (int i = 0; i < curr.edges.size(); i++) {
		// if read value is equal to given c, go to pointsTo state
		if (curr.edges.get(i).trans[1].equals(readVal)) {
		    found = true;
		    String change2Val = curr.edges.get(i).trans[2];
		    inputSB.setCharAt(idx, change2Val.charAt(0));
		    if (idx == inputSB.length() - 1) {
			inputSB.append("*");
		    } else if (idx == 0) {
			inputSB.insert(0, "*");
			idx += 1;
		    }
		    String direction = curr.edges.get(i).trans[3];
		    curr = curr.goToNext(readVal);
		    if (curr == null) {
			return "Input string not accepted";
		    }
		    if (direction.equals("L")) {
			idx--;
		    } else if (direction.equals("R")) {
			idx++;
		    }
		    break;
		}
	    }
	    if (found == false) {
		return "Input string not accepted";
	    }
	}

	if (curr.isAcceptState == false) {
	    return "Input string not accepted";
	} else {
	    int left = 0;
	    while (inputSB.charAt(left) == '*') {
		left++;
	    }
	    int right = inputSB.length() - 1;
	    while (inputSB.charAt(right) == '*') {
		right--;
	    }
	    return inputSB.toString().substring(left, right + 1);
	}
    }

    class Node {

	String stateName;
	ArrayList<Edge> edges;
	boolean isAcceptState;

	Node(String stateName) {
	    this.stateName = stateName;
	    this.edges = new ArrayList<>();
	    this.isAcceptState = false;
	}

	Node goToNext(String c) {
	    for (int i = 0; i < this.edges.size(); i++) {
		// if read value is equal to given c, go to pointsTo state
		if (this.edges.get(i).trans[1].equals(c)) {
		    return this.edges.get(i).pointsTo;
		}
	    }
	    return null;
	}

	String getDirection(String c) {
	    String direction = null;
	    for (int i = 0; i < this.edges.size(); i++) {
		// if read value is equal to given c, go to pointsTo state
		if (this.edges.get(i).trans[1].equals(c)) {
		    direction = this.edges.get(i).trans[4];
		}
	    }
	    return direction;
	}

	void addEdge(Edge e) {
	    this.edges.add(e);
	}

	void changeToAcceptState() {
	    this.isAcceptState = true;
	}

	boolean isAcceptState() {
	    return this.isAcceptState;
	}

    }

    class Edge {
	// if read 0, change it to 1 and go to 2 (left or right)
	String[] trans;
	Node pointsTo;

	Edge(String[] transition, Node to) {
	    this.trans = transition;
	    this.pointsTo = to;
	}
    }
}
