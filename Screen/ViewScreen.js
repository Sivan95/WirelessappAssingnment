import React, {Component} from 'react';
import {
    Text, FlatList, View, StyleSheet, TouchableHighlight,
} from 'react-native';
import { FloatingAction } from 'react-native-floating-action';
console.disableYellowBox = true; //to avoid the warning
let SQLite = require('react-native-sqlite-storage'); // to load the sqlite file
let config = require('./Config');

export default class VieScreen extends Component{

    static navigationOptions = {
        title: 'MY TOURIST APP',
    }

    constructor(props) {
        super(props)

        this.state = {
          places: [],
          isFetching : false,
        };

        this._query = this._query.bind(this);
        this._load = this._load.bind(this);

        this.db = SQLite.openDatabase({
          name: 'place',
          createFromLocation : '~place.sqlite'
        }, this.openDb, this.errorDb);
      }

      componentDidMount() {
        this._query();
        this._load();
      }

      _query() {
        let id = this.props.navigation.getParam("selectedStateId")
        //alert(id)
        this.db.transaction((tx) => {
          tx.executeSql(`SELECT * FROM places WHERE state = ?` , [
            id
          ], (tx, results) => {
            this.setState({
              places: results.rows.raw(),
            })
          })
        });
      }

      openDb() {
          console.log('Database opened');
      }

      errorDb(err) {
          console.log('SQL Error: ' + err);
      }
      _load(){
        let url = config.settings.serverPath;
        let url_url = url + '/api/places/state/view/' + this.props.navigation.getParam('selectedStateId');

        this.setState({isFetching: true});
        console.log(url_url);
        fetch(url_url,{method: 'GET',
        headers:{
          Accept: 'application/json',
          'Content-Type': 'application/json',
        }})
        .then((response) => {
          if(!response.ok){
            Alert.alert('Error', response.status.toString());
            throw Error('Error'+ response.status);
          }
          return response.json()
        })
        .then((places) => {
          this.setState({places:places});
          this.setState({isFetching:false});
        })
        .catch((error) => {
          console.log(error)
        });
      }
    render(){
        return(
            <View style={styles.container}>

            <FlatList
                data={ this.state.places }
                extraData={this.state}
                showsVerticalScrollIndicator={ true }
                renderItem={({item}) =>
                    <TouchableHighlight
                    underlayColor={'#cccccc'}
                    onPress={ () => {
                        this.props.navigation.navigate('DetailScreen', {
                        id: item.id,
                        headerTitle: item.title,
                        refresh: this._query,
                        refresh: this._load,
                        })
                    }}
                    >
                    <View style={styles.item}>
                        <Text style={styles.itemLocation}>{ item.location }</Text>
                        <Text style={styles.itemName}>Tourist Spot : { item.name }</Text>
                    </View>

                    </TouchableHighlight>
                }
                keyExtractor={(item) => {item.id.toString()}}
            />
            </View>
        );
    }
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      justifyContent: 'flex-start',
      backgroundColor: '#3366cc',
    },
    item: {
      justifyContent: 'center',
      paddingTop: 10,
      paddingBottom: 10,
      paddingLeft: 25,
      paddingRight: 25,
      borderBottomWidth: 1,
      borderColor: '#660066',
    },
    itemLocation: {
      fontSize: 30,
      fontWeight: '500',
      color: '#000',

    },

    itemName: {
      fontSize: 17,
      color: 'black',
      fontWeight: '500',
    },
  });
