import React, { Component } from 'react';
import {
  Platform,
  StyleSheet,
  Text,
  View,
} from 'react-native';
console.disableYellowBox = true; //to avoid the warning
import MainServices from './MainServices';
export default class LoadingScreen extends Component<Props>{
  static navigationOptions = {
    title: 'MY TOURIST APP',
  };
  state = {
    loaded: false
  }
  constructor(){
    super();
    MainServices.load(v => this.setState({loaded:true}));
  }
  render(){
    return(
      <View style={styles.container}>
        {this.state.loaded ? this.props.navigation.navigate('HomeScreen') :
          <Text style={styles.text}>
            {`WELCOME TO TOURIST APP\n
                Loading.....`}
          </Text>}
      </View>
    );
  }
}
const styles = StyleSheet.create({
  container:{
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#00ffff',
  },
  text:{
    color: '#000000',
    fontSize: 30,
    fontWeight: 'bold',
    alignItems: 'center',
    justifyContent: 'center',
    paddingBottom: 4,
  }

});
