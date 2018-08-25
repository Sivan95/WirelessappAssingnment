import {
  createStackNavigator,
} from 'react-navigation';
import HomeScreen from './Screen/HomeScreen';
import ViewScreen from './Screen/ViewScreen';
import DetailScreen from './Screen/DetailScreen';
import LoadingScreen from'./Screen/LoadingScreen';

export default createStackNavigator({
  LoadingScreen:{
    screen: LoadingScreen,
  },
  HomeScreen: {
    screen: HomeScreen,
  },
  ViewScreen: {
    screen: ViewScreen,
  },
  DetailScreen: {
    screen: DetailScreen,
  },
}, {
  initialRouteName: 'LoadingScreen',
});
