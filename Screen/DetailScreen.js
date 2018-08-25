import React, {Component} from 'react';
import {
    Text, View, ScrollView, StyleSheet,
} from 'react-native';
import {InputWithLabel} from './UI';
let SQLite = require('react-native-sqlite-storage');
let config = require('./Config');

export default class DetailScreen extends Component{

    static navigationOptions = {
      title: 'MY TOURIST APP',
    }

      constructor(props) {
        super(props)

        this.state = {
          placesId: this.props.navigation.getParam('id'),
          places: [],
          isFetching : false,
        };

        this._query = this._query.bind(this);
        this._load = this._load.bind(this);
        this.db = SQLite.openDatabase({name: 'place', createFromLocation : '~place.sqlite'}, this.openDb, this.errorDb);
      }

      componentDidMount() {
        this._query();
        this._load();
      }


      _query() {
        this.db.transaction((tx) => {
          tx.executeSql('SELECT * FROM places WHERE id = ?', [this.state.placesId], (tx, results) => {
            if(results.rows.length) {
              this.setState({
                places: results.rows.item(0),
              })
            }
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
      let url_url = url + '/api/places/state/detail/' + this.props.navigation.getParam('placesId');

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
        let places = this.state.places;
        {console.log(places)}
        return(
            <View style={styles.container}>
                <ScrollView>
                    <InputWithLabel style={styles.output}
                        multiline = {true}
                        label={'Location'}
                        value={places ? places.location : ''}
                        orientation={'vertical'}
                        editable={false}
                    />
                    <InputWithLabel style={styles.output}
                        multiline = {true}
                        label={'Tourist Spot'}
                        value={places ? places.name : ''}
                        orientation={'vertical'}
                        editable={false}
                    />
                    <InputWithLabel style={styles.output}
                        multiline = {true}
                        label={'Address'}
                        value={places ? places.address : ''}
                        orientation={'vertical'}
                        editable={false}
                    />

                    <InputWithLabel style={styles.output}
                        multiline = {true}
                        label={'Additional Info'}
                        value={places ? places.description : ''}
                        orientation={'vertical'}
                        editable={false}
                    />

                </ScrollView>
            </View>
        );
    }
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      padding: 20,
      backgroundColor: '#bfbfbf',
    },
    output: {
      fontSize: 20,
      fontWeight: 'bold',
      color: '#000099',
      marginTop: 10,
      marginBottom: 10,
      borderBottomWidth: 1,
      borderColor: '#660066',
    },
  });
