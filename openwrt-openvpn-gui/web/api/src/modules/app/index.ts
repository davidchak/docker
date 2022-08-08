import express, {Express} from "express";
import { createServer } from "http";

class App {
  router: Express; 
  port: string | number;
  server: typeof createServer;
    
  constructor(){
    this.router = express();
    this.port = process.env.PORT || 5000;
    this.server = createServer;
  }
    
  start(){
    this.server(this.router)
      .listen(this.port, () => {
        console.info(`Server started at http://localhost:${this.port}`)
      })
  }   
}

export default App;