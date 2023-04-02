export interface UserCredentials {
    username: string,
    password: string
  }
 
  export interface LoggedInUser {
    user_id: number,
    token: string,
    is_patient:boolean,
  }