import React, { Component } from 'react';
import {
  StyleSheet,
  TextInput,
  Text,
  ScrollView,
  TouchableOpacity
} from 'react-native';
import {
  PickerWithLabel,
  AppButton,
} from './UI';

let common = require('./CommonData');
let SQLite = require('react-native-sqlite-storage');
let config = require('./Config');

type Props = {};
export default class HomeScreen extends Component<Props> {
  static navigationOptions = {
    title: 'MY TOURIST APP',
  };

  constructor(props) {
    super(props)

    this.state = {
      places: [],
      isFetching: false,
      selectedStateId: '',
      noneselectedStateId: true,
    };

    this._load = this._load.bind(this);
    this._query = this._query.bind(this);

    this.db = SQLite.openDatabase({
      name: 'place',
      createFromLocation : '~place.sqlite'
    }, this.openDb, this.errorDb);
  }
  openDb(){
    console.log('Database opened succesfully');
  }
  errorDb(err){
    console.log('Error occured', err);
  }
  _query(theState){
    this.db.transaction((tx) => {
      tx.executeSql('INSERT into places(state) values(?)',[theState])
    })
  }
  componentDidMount() {
    this._load();
    this._query();
  }

  _load() {
    let url = config.settings.serverPath + '/api/places/state/';
    let url_url= '';
    if(this.state.noneselectedStateId){
      url_url = url;
    }
    else{
      url_url = url + this.state.selectedStateId;
    }
    this.setState({isFetching: true});
    console.log(url_url);
    fetch(url_url,{
      method: 'GET',
      headers:{
        'Accept':'application/json',
        'Content-Type': 'application/json',
      }})
    .then((response) => {
      if(!response.ok) {
        Alert.alert('Error', response.status.toString());
        throw Error('Error ' + response.status);
      }
      return response.json()
    })
    .then((places) => {
      this.setState({places:places});
      this.setState({isFetching: false});
    })
    .catch((error) => {
      console.log(error)
    });
  }

  render(){
    return(
      <ScrollView style = {styles.container}>
        <PickerWithLabel style = {styles.picker}
          label = {'STATE:'}
          prompt={'Select State'}
          items = {common.states}
          mode = {'dialog'}
          value = {this.state.selectedStateId}
          enabled={'enabled'}
          onValueChange={(itemValue, itemIndex) => {
            this.setState({
              selectedStateId: itemValue,
              noneselectedStateId: false,
            })
        }}
        />
          <AppButton style={styles.button}
          title={'Search'}
          theme = {'primary'}
          onPress={
            () => {
              this.props.navigation.navigate('ViewScreen',
              {
                selectedStateId : this.state.selectedStateId,
              })
            }
          }
          />
      </ScrollView>
    );
  }
}
  const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#00ffff',
  },
  picker: {
    color: '#000099',
    marginTop: 10,
    marginBottom: 10,
    fontSize: 50,
  },
});
