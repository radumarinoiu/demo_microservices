package test.microservis;

import com.sun.javafx.beans.IDProperty;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/site")
public class Clasa {

    private Altceva foo;

    @GetMapping("/home")
    public Altceva mesaj(){
        foo = new Altceva(2, 8);
        return foo;
    }
}
