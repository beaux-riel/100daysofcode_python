// Very cool.

// How to create a class in React Native?

//Within TypeScript, React.Component is a generic type (aka React.Component<PropType, StateType>), so you want to provide it with (optional) prop and state type parameters:
type MyProps = {  // using `interface` is also ok  message: string;};type MyState = {  count: number; // like this};class App extends React.Component<MyProps, MyState> {  state: MyState = {    // optional second annotation for better type inference    count: 0,  };  render() {    return (      <div>        {this.props.message} {this.state.count}      </div>    );  }}

//You often see sample code include readonly to mark props and state immutable:
type MyProps = {  readonly message: string;};type MyState = {  readonly count: number;};

//Class Methods: Do it like normal, but just remember any arguments for your functions also need to be typed:
class App extends React.Component<{ message: string }, { count: number }> {  state = { count: 0 };  render() {    return (      <div onClick={() => this.increment(1)}>        {this.props.message} {this.state.count}      </div>    );  }  increment = (amt: number) => {    // like this    this.setState((state) => ({      count: state.count + amt,    }));  };}

//Class Properties: If you need to declare class properties for later use, just declare it like state, but without assignment:
class App extends React.Component<{  message: string;}> {  pointer: number; // like this  componentDidMount() {    this.pointer = 3;  }  render() {    return (      <div>        {this.props.message} and {this.pointer}      </div>    );  }}

//If you have explicitly typed your derived state and want to make sure that the return value from getDerivedStateFromProps conforms to it.
class Comp extends React.Component<Props, State> {  static getDerivedStateFromProps(    props: Props,    state: State  ): Partial<State> | null {    //  }}

//When you want the function's return value to determine your state.
class Comp extends React.Component<  Props,  ReturnType<typeof Comp["getDerivedStateFromProps"]>> {  static getDerivedStateFromProps(props: Props) {}}

//When you want derived state with other state fields and memoization
type CustomValue = any;interface Props {  propA: CustomValue;}interface DefinedState {  otherStateField: string;}type State = DefinedState & ReturnType<typeof transformPropsToState>;function transformPropsToState(props: Props) {  return {    savedPropA: props.propA, // save for memoization    derivedState: props.propA,  };}class Comp extends React.PureComponent<Props, State> {  constructor(props: Props) {    super(props);    this.state = {      otherStateField: "123",      ...transformPropsToState(props),    };  }  static getDerivedStateFromProps(props: Props, state: State) {    if (isEqual(props.propA, state.savedPropA)) return null;    return transformPropsToState(props);  }}

